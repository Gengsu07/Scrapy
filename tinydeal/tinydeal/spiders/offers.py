import scrapy

class OffersSpider(scrapy.Spider):
    name = 'offers'
    allowed_domains = ['web.archive.org']
    start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']

    def start_requests(self):
       yield scrapy.Request(url='https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html',callback=self.parse,
                            headers={
                                'User-Agent':'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
                            })
        

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
                'original_price':original_price,
                'user-agent':response.request.headers['User-Agent']
            }

        #locate next page button
        next_page = response.xpath('//a[@class="nextPage"]/@href').get()
        
        #request ke halaman selanjutnya jika tombol nextpage available
        if next_page:
         yield scrapy.Request(url=next_page,callback=self.parse, headers={
             'User-Agent':'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
         })