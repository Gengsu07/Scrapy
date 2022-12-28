import scrapy


class GdpDeptSpider(scrapy.Spider):
    name = 'gdp_dept'
    allowed_domains = ['webscraper.io']
    start_urls = ['https://webscraper.io/test-sites/tables/']

    def parse(self, response):
        # table = response.xpath('//tbody[@class="jsx-a3119e4553b2cac7"]')
        rows = response.xpath("//table/tbody/tr")
        for row in rows:
            country = row.xpath('.//td[1]/a/text()').get()
        #     for col in row:
        #         country = col.xpath('.//td/a/text()').get()
        #         link = col.xpath('.//td/a/@href').get()
        #         debt_to_gdp = col.xpath('.//td[2]/text()').get()
        #         population = col.xpath('.//td[3]/text()').get()
            yield {
                'country':country
                # 'country':country,
                # 'link':link,
                # 'debt_to_gdp':debt_to_gdp,
                # 'population':population
            }
            
