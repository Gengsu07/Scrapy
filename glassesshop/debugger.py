import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from glassesshop.spiders.bestseller import BestsellerSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(BestsellerSpider)
process.start()