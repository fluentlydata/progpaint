import scrapy
from scrapy.selector import Selector

class TestSpider(scrapy.Spider):
    name = 'complete'
    start_urls = ['http://classicprogrammerpaintings.com/']

    def parse(self, response):

        def strip_join(txtarray):
          a = [ x.lstrip().rstrip() for x in txtarray ]
          return " ".join(a)

        # probably better:
        # Selector(response=r).xpath('//section[@class="post"]/node()').extract()
        for p in Selector(response=response).xpath('//article//node()').extract():
            print(p)
            yield {
                'img': Selector(text=p).css('img::attr("src")').extract_first(),
                'text': strip_join(Selector(text=p).xpath('//text()').extract()), # contains too many \r and \n
            }

            # xpath('//figcaption[@class="caption"]//text()')

        # and extract
        # 1.

        # 2. select the pre-tag ('import java.lang.reflect.*;')
        #

        # 3. select the remaining p-tags
        #

        # questions = Selector(response).xpath('//div[@class="summary"]/h3')

        # for question in questions:
        #     item = TestItem()
        #     item['title'] = question.xpath(
        #         'a[@class="question-hyperlink"]/text()').extract()[0]
        #     item['url'] = question.xpath(
        #         'a[@class="question-hyperlink"]/@href').extract()[0]
        #     yield item
