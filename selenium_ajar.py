from time import sleep
import schedule 
import random
import pymongo
import urllib
from apscheduler.schedulers.blocking import BlockingScheduler
# from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
# req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
# proxies = req_proxy.get_proxy_list() #this will create proxy list
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
import os
# CHROMEDRIVER_PATH = r"C:\Users\G RAJA\Desktop\scrapy_mongo\scraper\chromedriver.exe"
# GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
# CHROMEDRIVER_PATH = "./chromedriver"

GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = GOOGLE_CHROME_PATH
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

delay = 3
ua = UserAgent()
def some_job():
    print("called for job")
    for i in range(1, 27000):
        print(i)
        userAgent = ua.random
        print(userAgent)
        chrome_options.add_argument(f'user-agent={userAgent}')
        # PROXY = "socks5://localhost:9050"
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
#         PROXY = "socks5://localhost:9050"
#         chrome_options.add_argument('--proxy-server=%s' % PROXY)
        browser = webdriver.Chrome(
                executable_path=CHROMEDRIVER_PATH,
                chrome_options=chrome_options,
            )
        url = f"https://ajarani.me/item/{i}"        
        browser.get(url=url)
        time_1 = random.randint(5,7)
        sleep(time_1)
        try:
            element = browser.find_element_by_xpath('//*[@id="exoNativeWidget4042496"]/div[2]/div[1]/a')
            element.click()
            element = browser.find_element_by_xpath('//*[@id="exoNativeWidget4042496"]/div[2]/div[2]/a')
            element.click()
            time_2 = random.randint(5,7)
            sleep(time_2)
            print("clicked")
        except: 
            print("no <a> tag! maybe page not loaded fully")
        
        time_3 = random.randint(2,4)    
        sleep(time_3)
        print("success")
        browser.quit()
for i in range(2, 4):
    userAgent = ua.random
    print(userAgent)
    chrome_options.add_argument(f'user-agent={userAgent}')
    # PROXY = "socks5://localhost:9050"
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
#     PROXY = "socks5://localhost:9050"
#     chrome_options.add_argument('--proxy-server=%s' % PROXY)
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--ignore-ssl-errors')
    browser = webdriver.Chrome(
            executable_path=CHROMEDRIVER_PATH,
            chrome_options=chrome_options,
        )
    url = f"https://ajarani.me/item/{i}"        
    browser.get(url=url)
    time_1 = random.randint(5,7)
    sleep(time_1)
    try:
        
        element = browser.find_element_by_xpath('//*[@id="exoNativeWidget4042496"]/div[2]/div[1]/a')
        element.click()
        element = browser.find_element_by_xpath('//*[@id="exoNativeWidget4042496"]/div[2]/div[2]/a')
        element.click()
        # element = browser.find_element_by_xpath('//*[@id="container-c5df4e3fd9c30eb6a6083deb83df6ebd"]/div[2]/div[1]/div/a')
        # element.click()
        # except:
        #     print("second failed")
        time_2 = random.randint(5,7)
        sleep(time_2)
        print("clicked")
    except: 
        print("no <a> tag! maybe page not loaded fully")
    time_3 = random.randint(2,4)    
    sleep(time_3)
    print("success")
    browser.quit()
schedule.every(1).minutes.do(some_job) 
while True: 
  
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    sleep(1)
# scheduler = BlockingScheduler()
# scheduler.add_job(some_job, 'interval', minutes=30)
# scheduler.start()
# 22584 
# ubuntu@ec2-3-23-208-172.us-east-2.compute.amazonaws.com
# tmux new -s mywindow // runs continously even exited
# python selenium_ajar.py // run after above command and safely exit the aws instance sesssion
# tmux a -t mywindow // use to view the process and terminate
# tmux new -s traffic1