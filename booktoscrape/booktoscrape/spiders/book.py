import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//article[@class="product_pod"]/h3'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]'))
    )

    def parse_item(self, response):
        title = response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get()
        price = response.xpath('//p[@class="price_color"]/text()').get()
        stock = response.xpath('normalize-space(//p[@class="instock availability"]/text()[2])').get()
        yield {
            'title':title,
            'price':price,
            'stock' :stock
        }
        
