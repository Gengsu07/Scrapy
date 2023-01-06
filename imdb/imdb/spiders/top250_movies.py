import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Top250MoviesSpider(CrawlSpider):
    name = 'top250_movies'
    allowed_domains = ['web.archive.org','imdb.com']
    start_urls = ['http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating']

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    
    def start_requests(self):
        yield scrapy.Request(url='http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating',
                             headers={'User-Agent':self.user_agent})
         
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3[@class="lister-item-header"]'), callback='parse_item', follow=True, process_request='set_useragent'),
        Rule(LinkExtractor(restrict_xpaths='(//a[@class="lister-page-next next-page"])[2]'),process_request='set_useragent')
    )
    
    def set_useragent(self,request,spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        title = response.xpath('//div[@class="title_wrapper"]/h1/text()').get()
        year = response.xpath('//span[@id="titleYear"]/a/text()').get()
        duration = response.xpath('//div[@class="txt-block"]/time/text()').get()
        genre = response.xpath('//div[@class="subtext"]/a[1]/text()').get()
        rating = response.xpath('//span[@itemprop="ratingValue"]/text()').get()
        url = response.url,
        user_agent = response.request.headers['User-Agent']
        yield {
            'title':title,
            'year':year,
            'duration' :duration,
            'genre':genre,
            'rating': rating,
            'url':url,
            'user_agent':user_agent
        }