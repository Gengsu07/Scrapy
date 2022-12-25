import scrapy


class PopulationSpider(scrapy.Spider):
    name = 'population'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        # link = response.xpath("//td/a/@href").getall()
        for country in countries:
            name = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()
            yield {
                'country':name,
                "link":link
            }
