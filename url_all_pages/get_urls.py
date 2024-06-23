import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MySpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["https://filmot.com/search/%22under+my%22%2C+%22longing+for%22%2C+%22answer%22%2C+%22every%22%2C+%22where%22/1?sortField=viewcount&sortOrder=asc&gridView=1&"]
    
    def __init__(self):
        self.driver = webdriver.Firefox()  # Replace with your preferred browser


    def iterates(self,begin, end):
        for s in range(begin,end):
            try:
                button = WebDriverWait(self.driver, 40).until(
                    EC.element_to_be_clickable((By.ID, "moreResults"))
                )
                button.click()
                # Wait for the page to load
                self.driver.implicitly_wait(35)
                current_url = self.driver.current_url
                yield {"url": current_url}
            except:
                break    
    def parse(self, response):
        self.driver.get(response.url)
        current_url = self.driver.current_url
        yield {"url": current_url}
        for url in self.iterates(0,84):
            yield url
        for url in self.iterates(84,168):
            yield url
