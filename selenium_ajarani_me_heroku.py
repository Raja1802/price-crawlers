# runs in oracle cloud
from time import sleep
import random
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from fake_useragent import UserAgent
import os
import json
delay = 0
ua = UserAgent()
GOOGLE_CHROME_PATH = "/app/.apt/usr/bin/google-chrome"
CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
m=0
def some_job():
    for i in range(0, 200000):
        userAgent = ua.random
        print(userAgent)
        PROXY = "socks5://localhost:9050"
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument(f'user-agent={userAgent}')
        # chrome_options.add_argument('--proxy-server=%s' % PROXY)
        driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options,)
        episode_id = random.randint(126871, 253992)
        url = f"https://ajarmailer.ga/episode/{episode_id}"
        try:
            driver.get(url=url)
            sleep(1)
        except:
            driver.get(url="https://ajarmailer.ga/episode/126871")
        ran = 8
        if(m%ran == 0):
            time_1 = random.randint(3,5)
            sleep(time_1)
            try:
                sleep(5)
                ran_frame = random.randint(4,6)
                driver.switch_to.frame(ran_frame)
                sleep(2)
                options = driver.find_element_by_tag_name('a')
                options.click()
                sleep(6)
                print("clicked")
            except: 
                print("no <a> tag! maybe page not loaded fully")
        m = m+1
        print("success")
        driver.quit()
for i in range(0, 200000):
    userAgent = ua.random
    print(userAgent)
    PROXY = "socks5://localhost:9050"
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument(f'user-agent={userAgent}')
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options,)
    episode_id = random.randint(126871, 253992)
    url = f"https://ajarmailer.ga/episode/{episode_id}"
    try:
        driver.get(url=url)
        sleep(1)
    except:
        driver.get(url="https://ajarmailer.ga/episode/126871")  
    ran = 8
    if(m%ran == 0):
        time_1 = random.randint(3,5)
        sleep(time_1)
        try:
            sleep(3)
            ran_frame = random.randint(4,6)
            driver.switch_to.frame(ran_frame)
            sleep(2)
            options = driver.find_element_by_tag_name('a')
            options.click()
            sleep(6)
            print("clicked")
        except: 
            print("no <a> tag! maybe page not loaded fully")
    m = m+1
    driver.quit()
scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours=1)
scheduler.start()

# asaa