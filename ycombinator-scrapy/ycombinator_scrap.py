import csv

import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.reactor import install_reactor

class MySpider(scrapy.Spider):
    # Def des variables de notre spider
    # Nom
    name = 'ycombinator_spider'
    # Page courante que l'on traite dans l'iteration x.
    count_page:int = 0
    # Limite des page que l'on va traiter.
    page_limit:int = 2
    # Url de depart pour que la spider se lance - on pourrait faire autrement.
    start_url:str = "https://news.ycombinator.com/?p=0"
    # Url sans parametres.
    url:str = "https://news.ycombinator.com"

    # List de dict contenant la data que l'on va traiter
    data:list[dict] = []

    # Fonction usuelle disponible dans la doc, demarre le crawl.
    def start_requests(self):
        # Start with just one URL
        yield scrapy.Request(self.start_url, callback=self.parse)

    # Fonction qui va fetch les parameters
    def parse(self, response):
        print(f"### PAGE {self.count_page} ###")

        # Voir html de la page pour plus de comprehension.
        # On va recuperer la table contenant les donnees
        # table > tr > table
        table = response.xpath('//table[@id="hnmain"]//tr[@id="bigbox"]//table')[0]
        rows = table.xpath('.//tr')
        # Init du dict - on va stocker les donnees en iterant sur chaque ligne puis vider quand on fait le passage sur la ligne 1 puis 2.
        # La ligne 3 (space) est ingnoree.
        raw_data:dict = {}
        for row in rows:
            story_id = row.xpath('./@id').get()
            if story_id != None:
                raw_data["title"] = row.xpath('.//span[@class="titleline"]/a/text()').get()
                raw_data["source"] = row.xpath('.//span[@class="titleline"]/a/@href').get()
        
            if row.xpath('.//span[@class="subline"]'):
                upvotes:str = row.xpath('.//span[@class="score"]/text()').get()
                raw_data["upvote"] = int(upvotes.split(" ")[0])

                yield raw_data
                self.data.append(raw_data)
                raw_data:dict = {}

        # On passe a la prochaine page jusque la limite fixee au depart.
        self.count_page += 1
        if self.count_page < self.page_limit:
            yield response.follow(self.url + f"/?p={self.count_page}", self.parse)

# Config usuelle disponible dans la doc.
# Doc : https://docs.scrapy.org/en/latest/topics/asyncio.html
# Reactor : Permet de faire des requetes asynchrones - c'est le reactor le plus commun
install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
configure_logging({
    "LOG_FORMAT": "%(levelname)s: %(message)s",
    "LOG_LEVEL": "INFO"
})

# Init du runner pour lancer notre spider
runner = CrawlerRunner({
    'USER_AGENT': 'MySpider (+https://news.ycombinator.com)',
    'ROBOTSTXT_OBEY': True,
    'DOWNLOAD_DELAY': 1,
    'LOG_LEVEL': 'INFO'
})

# Config de la limite de pages puis on lance le crawl
MySpider.page_limit = 10
d = runner.crawl(MySpider)

from twisted.internet import reactor
d.addBoth(lambda _: reactor.stop())
reactor.run()

keys = MySpider.data[0].keys()
with open('rows.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(MySpider.data)
