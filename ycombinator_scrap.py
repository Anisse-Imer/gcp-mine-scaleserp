import csv

import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.reactor import install_reactor

class MySpider(scrapy.Spider):
    name = 'ycombinator_spider'
    count_page:int = 0
    page_limit:int = 2
    start_url:str = "https://news.ycombinator.com/?p=0"
    url:str = "https://news.ycombinator.com"

    data:list[dict] = []

    def start_requests(self):
        # Start with just one URL
        yield scrapy.Request(self.start_url, callback=self.parse)

    def parse(self, response):
        print(f"### PAGE {self.count_page} ###")

        table = response.xpath('//table[@id="hnmain"]//tr[@id="bigbox"]//table')[0]
        rows = table.xpath('.//tr')
        raw_data:dict = {

        }
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

        self.count_page += 1
        if self.count_page < self.page_limit:
            yield response.follow(self.url + f"/?p={self.count_page}", self.parse)

install_reactor("twisted.internet.asyncioreactor.AsyncioSelectorReactor")
configure_logging({
    "LOG_FORMAT": "%(levelname)s: %(message)s",
    "LOG_LEVEL": "INFO"
})

runner = CrawlerRunner({
    'USER_AGENT': 'MySpider (+https://news.ycombinator.com)',
    'ROBOTSTXT_OBEY': True,
    'DOWNLOAD_DELAY': 1,
    'LOG_LEVEL': 'INFO'
})

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
