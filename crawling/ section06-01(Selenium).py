# Section06-01
# Selenium
# Selenium 사용 실습(1) - 설정 및 기본 테스트

# https://sites.google.com/a/chromium.org/chromedriver/downloads

# selenium 임포트
from selenium import webdriver

# webdriver 설정(Chrome, Firefox 등)
browser = webdriver.Chrome('./webdriver/chromedriver')
