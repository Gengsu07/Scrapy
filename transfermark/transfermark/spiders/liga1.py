import scrapy


class Liga1Spider(scrapy.Spider):
    name = 'liga1'
    allowed_domains = ['www.transfermarkt.co.id']
    start_urls = ['https://www.transfermarkt.co.id/bri-liga-1/startseite/wettbewerb/IN1L/']

    def parse(self, response):
        klubs = response.xpath("//div[@id='yw1']/table/tbody/tr")
        for klub in klubs:
            tim = klub.xpath('.//td[2]/a/text()').get()
            link = klub.xpath('.//td[2]/a/@href').get()
            
            yield response.follow(link, callback = self.datapemain, meta={'klub':tim})
            
    def datapemain(self,response):
        klub = response.meta['klub']
        pemain = response.xpath(".//div[@id='yw1']/table/tbody/tr")
        for player in pemain:
            nama = player.css(".hide-for-small a ::text").get()
            posisi = player.xpath(".//td[2]/table/tr[2]/td/text()").get()
            ttl = player.xpath(".//td[4]/text()").get()
            value = player.xpath(".//td[6]/a/text()").get()
            yield{
                'nama':nama,
                'posisi':posisi,
                'ttl':ttl,
                'value':value,
                'klub':klub
            }
