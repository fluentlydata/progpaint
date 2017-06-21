import scrapy
from scrapy.selector import Selector

class TestSpider(scrapy.Spider):
    name = 'artist'
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    def parse(self, response):
        pass
