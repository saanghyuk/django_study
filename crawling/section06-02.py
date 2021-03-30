# Section06-02
# Selenium

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우져가 실행되지 않음.

# webdriver 설정(Chrome, Firefox 등) - Headless
browser = webdriver.Chrome('./webdriver/chromedriver', options=chrome_options)

