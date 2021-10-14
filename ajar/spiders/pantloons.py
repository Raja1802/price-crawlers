import scrapy
from ajar.items import AmazonUs
from scrapy.spiders import CrawlSpider, Rule, SitemapSpider
from selenium import webdriver
from time import sleep
from scrapy.selector import Selector
import json
import os
from scrapy.linkextractors import LinkExtractor as sle
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
ua = UserAgent()
# chrome requirments
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.binary_location = GOOGLE_CHROME_PATH


class QuotesInfiniteScrollSpider(CrawlSpider):
    name = "pantlon"
    rotate_user_agent = True
    allowed_domains = ["www.pantaloons.com"]
    start_urls = []
    # rules = (Rule(sle(allow="/p/", deny=("/c/", )), callback="parse_result", follow=True),)
    #sitemap_urls = ["https://www.pantaloons.com/product-sitemap.xml"]
    # parsing results with below function
    def parse(self, response):
        amazon = []
        amazon = AmazonUs()
        userAgent = ua.random
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument(f'user-agent={userAgent}')
        browser = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options,
        )
        browser.get(response.url)
        sleep(0.2)
        scrapy_selector = Selector(text=browser.page_source)
        # css selection of html data tags
        product_id = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_mrp = (
            scrapy_selector.css(
                "#divProductPrice > div > span.price::text"
            ).getall()
            or scrapy_selector.css("#divProductPrice > div > h1::text").getall()
        )
        product_description = (
            scrapy_selector.css(
                "#prod_desc > p::text"
            ).getall()
               )
        product_name = (
            scrapy_selector.css(
                "#pt_product_infodet > div > div.row > div > h2::text"
            ).getall()
              )
        product_ASIN = scrapy_selector.css(
            'head > link[rel= "canonical"]::attr(href)'
        ).get()
        product_by_url = "www.pantaloons.com"
        product_by_name = "pantaloons"
        product_rating = "NAN"
        product_image = (
            scrapy_selector.css(
                "head > meta[property='og:image']::attr(content)"
            ).get()
            or scrapy_selector.css("head > meta[name='twitter:image']::attr(content)").get()
        )
        product_image_2 = (
            scrapy_selector.css(
                "ul#thumblist > div > div > li[data-slick-index='1'] > a > div > img::attr(src)"
            ).getall()
        )
        product_image_3 = (
            scrapy_selector.css(
                "ul#thumblist > div > div > li[data-slick-index='2'] > a > div > img::attr(src)"
            ).getall()
        )
        product_image_4 = (
            scrapy_selector.css(
                "ul#thumblist > div > div > li[data-slick-index='3'] > a > div > img::attr(src)"
            ).get()
        )
        product_price = (
            scrapy_selector.css(
                "#divProductPrice > h1::text"
            ).getall()
        )
        product_about = (
            scrapy_selector.css(
                "#prod_feature > p > span::text"
            ).getall()
        )
        product_keywords = scrapy_selector.css(
            "#pt_product_infodet > div > div.row > div > h2.brandName::text"
        ).getall()
        product_catlog = (
            scrapy_selector.css(
                "body > section > div.container.container_body_inner.scroll_head_top > div.row > div > span > li > a > span::text"
            ).getall()
        )
        product_price_2 = (
            scrapy_selector.css(
                "span.percentage_off::text"
            ).getall()
        )

        product_keywords_2 = (
            scrapy_selector.css(
                "#appContainer > div.content > div > div > div.prod-container > div > div.col-4 > div > p.prod-color::text"
            ).getall()
            or scrapy_selector.css("head > meta[name='keywords']::attr(content)").getall()
        )

        # append data to items
        amazon["product_id"] = product_id
        amazon["product_mrp"] = product_mrp
        amazon["product_description"] = product_description
        amazon["product_name"] = product_name
        amazon["product_ASIN"] = product_ASIN
        amazon["product_by_url"] = product_by_url
        amazon["product_by_name"] = product_by_name
        amazon["product_rating"] = product_rating
        amazon["product_image"] = product_image
        amazon["product_image_2"] = product_image_2
        amazon["product_image_3"] = product_image_3
        amazon["product_image_4"] = product_image_4
        amazon["product_price"] = product_price
        amazon["product_about"] = product_about
        amazon["product_keywords"] = product_keywords
        amazon["product_catlog"] = product_catlog
        amazon["product_price_2"] = product_price_2
        amazon["product_keywords_2"] = product_keywords_2
        browser.quit()
        return amazon


# git push change usage comments
# push 1
