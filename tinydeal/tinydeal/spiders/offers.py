import scrapy


class OffersSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    def parse(self, response):
        for product in response.xpath('//div[@ class="p_box_wrapper"]'):
            title = product.xpath('.//li/a[@class="p_box_title"]/text()').get()
            url = response.urljoin(product.xpath('.//li/a[@class="p_box_title"]/@href').get())
            discount_price = product.xpath('.//span[@class="productSpecialPrice fl"]/text()').get()
            original_price = product.xpath('.//span[@class="normalprice fl"]/text()').get()
            
            yield{
                'title':title,
                'url':url,
                'discout_price':discount_price,
                'original_price':original_price
            }
