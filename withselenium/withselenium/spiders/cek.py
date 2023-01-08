import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CekSpider(scrapy.Spider):
    name = 'cek'
   
    
    def start_request(self):
        yield  SeleniumRequest(
            url = 'https://duckduckgo.com',
            callback = self.parse,
            # wait_until=EC.element_to_be_clickable(By.XPATH,'//input[@class="js-search-input search__input--adv"]'),
            wait_time=3,
            screenshot=True
        )
        

    def parse(self, response):
        img = response.meta['screenshot']
        with open('img.png','wb') as screenshot:
            screenshot.write(img)
