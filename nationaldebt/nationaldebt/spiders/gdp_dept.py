import scrapy


class GdpDeptSpider(scrapy.Spider):
    name = 'gdp_dept'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/country-rankings/countries-by-national-debt/']

    def parse(self, response):
        table = response.xpath('//tbody[@class="jsx-a3119e4553b2cac7"]')
        for row in table.xpath('.//tr'):
            for col in row:
                country = col.xpath('.//td/a/text()').get()
                link = col.xpath('.//td/a/@href').get()
                debt_to_gdp = col.xpath('.//td[2]/text()').get()
                population = col.xpath('.//td[3]/text()').get()
            yield {
                'country':country,
                'link':link,
                'debt_to_gdp':debt_to_gdp,
                'population':population
            }
            
