import scrapy
from ajar.items import AmazonUs,SpecsExtractor,ImageExtractor,SpecImage
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
# import numpy as np
import json
import requests
import pymongo
import urllib
from pandas import json_normalize
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(scrapy.Spider):
    name = "puma_specs_data"
    rotate_user_agent = True
    allowed_domains = ["in.puma.com"]
    start_urls = []
    def start_requests(self):
        myclient = pymongo.MongoClient("mongodb://ajar:" + urllib.parse.quote_plus("Raja@1802") + "@links-shard-00-00.rjots.mongodb.net:27017,links-shard-00-01.rjots.mongodb.net:27017,links-shard-00-02.rjots.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-xypyrq-shard-0&authSource=admin&retryWrites=true&w=majority")
        mydb = myclient.LinksDB
        mycol = mydb.Links
        mydoc = mycol.find({"store_id": 33235})
        df = json_normalize(mydoc)
        df = df.drop_duplicates(subset="product_id", keep='first')
        # columns = ['product_id']
        # for column in columns:
        #     df[column] = df[column].astype(str)
        #     df[column] =  "https://www.flipkart.com" + df[column]
        # df.drop(df[df["url"] == "https://www.flipkart.comNAN"].index, inplace=True)
        # df = pd.read_csv(r"C:\Users\G RAJA\Desktop\ajarani.me\data\exports\AnimeApi\daily\converted_csv\07-02-2021.csv")
        # df2 = df.drop_duplicates(subset="ep_url" , keep='first')
        # df2 = df2.iloc[60000:]
        urls = []
        for index, row in df.iterrows():
            urls.append(row["product_id"])
        df = 0 
        mycol = 0
        mydoc = 0
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # rules = (Rule(sle(allow=( "shirt", "shoes","mobile","cycle","women","men","/p/"), deny=("product-reviews")), callback="parse_result", follow=True),)
    # parsing results with below function
    def parse(self, response):
        # amazon = []
        # ImageExtractor = {}
        # SpecsExtractor = {}
        # amazon = AmazonUs()
        # ImageExtractor = ImageExtractor()
        # SpecsExtractor = SpecsExtractor()
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        # sleep(0.5)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        for i in scrapy_selector.css("div.details"):
            pid = response.url
            specKey = "Detail"
            specValue = i.css("div.single-story-block > ul > li::text").get()
            yield SpecsExtractor(pid=pid,specKey=specKey,specValue=specValue)
            # return SpecsExtractor
        # for j in scrapy_selector.css("div._20Gt85"):
        #     ImageExtractor["image"] = j.css["div.q6DClP"].get()
        # yield SpecImage(images=ImageExtractor, specs=SpecsExtractor)
        browser.quit()
        # return amazon


# git push change usage comments
# push 1
