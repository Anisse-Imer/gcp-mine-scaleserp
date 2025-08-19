import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.reactor import install_reactor

class MySpider(scrapy.Spider):
    name = 'ycombinator_spider'
    count_page:int = 0
    page_limit:int = 5
    start_url:str = "https://news.ycombinator.com/?p=0"
    url:str = "https://news.ycombinator.com"

    def start_requests(self):
        # Start with just one URL
        yield scrapy.Request(self.start_url, callback=self.parse)

    def parse(self, response):
        table = response.xpath('table')
        print(table)
        rows = table.xpath('//tr')
        print(rows)

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

d = runner.crawl(MySpider)

from twisted.internet import reactor
d.addBoth(lambda _: reactor.stop())
reactor.run()
