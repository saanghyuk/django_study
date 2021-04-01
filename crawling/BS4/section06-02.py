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

# 크롬 브라우져 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print("Before Page Content : {}".format(browser.page_source))

# 제조사별 더 보기 클릭 1
# Explicity Wait
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()


# 제조사별 더 보기 클릭 2 이렇게 하면 진짜 2초를 풀로 기다림. 위의 예에서는 3초 전에라도 되면 누름
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭

# Apple
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[15]/label'))).click()
print("After Page Content : {}".format(browser.page_source))

time.sleep(2)

# bs4 초기화
soup = BeautifulSoup(browser.page_source, 'html.parser')

# 소스코드 정리
print(soup.prettify())

# 메인상품 리스트 선택
prod_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

# 상품 리스트 확인
# print(prod_list)

for v in prod_list:
  # print(v)
  if not v.find('div', class_="ad_header"):
    # 상품, 이미지, 가격
    try:
      print(v.select('p.prod_name > a')[0].text.strip())
      print('http:'+ v.select('a.thumb_link > img')[0]['data-original'])
      print(v.select('p.price_sect > a')[0].text.strip())
    except:
      pass

# 브라우저 종료
browser.close()
