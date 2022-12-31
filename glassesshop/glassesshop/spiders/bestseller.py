import scrapy


class BestsellerSpider(scrapy.Spider):
    name = 'bestseller'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for item in response.xpath('//div[@class="col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center product-list-item"]'):
            inside = len(item.xpath('.//div[@class="product-colors d-block d-lg-none product-colors-mobile-display"]'))+1
            for count in range(1,inside):
                name =  item.xpath(f'.//div[@class="p-title"]/a[{count}]/text()').get().strip()
                url = item.xpath(f'.//div[@class="p-title"]/a[{count}]/@href').get()
                image = item.xpath(f'.//div[@class="product-img-outer"]/a[{count}]/@href').get()
                price = item.xpath(f'.//div[@class="p-price"]/div[{count}]/span/text()').get()
                
                yield {
                    'name':name,
                    'url':url,
                    'imgurl':image,
                    'price':price
                }

        next_page = response.xpath('//a[@aria-label="Next »"]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page,callback=self.parse)