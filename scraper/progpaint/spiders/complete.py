import scrapy
import time
import datetime
from scrapy.selector import Selector
from progpaint.items import PostItem

class TestSpider(scrapy.Spider):
    name = 'complete'
    start_urls = ['http://classicprogrammerpaintings.com/']

    def parse(self, response):

        # timestamp
        tt = time.time()
        ts = datetime.datetime.fromtimestamp(tt).strftime('%Y-%m-%d %H:%M:%S')

        def strip_join(txtarray):
          a = [ x.lstrip().rstrip() for x in txtarray ]
          return " ".join(a)

        # p=post text
        def create_item(p):
          item = PostItem()
          item['image_urls'] = Selector(text=p).css('img::attr("src")').extract()
          item['text']       = strip_join(Selector(text=p).xpath('//text()').extract()) # contains too many \r and \n
          item['ts']         = ts
          return item

        # iterate through every post
        for p in Selector(response=response).xpath('//section[@class="post"]/node()').extract():
            yield create_item(p)

