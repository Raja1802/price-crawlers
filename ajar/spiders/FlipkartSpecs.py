import scrapy
from ajar.items import AmazonUs,SpecsExtractor,ImageExtractor,SpecImage
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from os import getcwd
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import json
import requests
import pymongo
import urllib
from pandas import json_normalize

GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH
from webdriver_manager.chrome import ChromeDriverManager



class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "flipkart_specs_data"
    rotate_user_agent = True
    allowed_domains = ["www.flipkart.com"]
    start_urls = []
    def parse(self, response):
        browser = webdriver.Chrome(
            # executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            executable_path=ChromeDriverManager().install(),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        # sleep(2) #
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tagscls
        for i in scrapy_selector.css("tr._1s_Smc") or scrapy_selector.css("div._13swYk > div.row"):
            pid = response.url
            specKey = i.css("td._1hKmbr::text").get()  or i.css("div._2H87wv").get()
            specValue = i.css("li._21lJbe::text").get() or i.css("div._2vZqPX").get()
            yield SpecsExtractor(pid=pid,specKey=specKey,specValue=specValue)
        # sleep(2)
        browser.quit()
        
                
