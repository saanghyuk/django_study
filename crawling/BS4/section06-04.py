# Section06-04
# Selenium

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 엑셀처리 임포트
import xlsxwriter
from io import BytesIO
import urllib.request as req

# 엑셀 처리 선언
workbook = xlsxwriter.Workbook("./resources/crawling_result.xlsx")

# 워크 시트
worksheet = workbook.add_worksheet()



chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우져가 실행되지 않음.

# webdriver 설정(Chrome, Firefox 등) - Headless
# browser = webdriver.Chrome('./webdriver/chromedriver', options=chrome_options)
browser = webdriver.Chrome('./webdriver/chromedriver')

# 크롬 브라우져 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280)

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print("Before Page Content : {}".format(browser.page_source))

# 제조사별 더 보기 클릭
# Explicity Wait
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 원하는 모델 카테고리 클릭
# Apple
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchMaker1452"]'))).click()
# print("After Page Content : {}".format(browser.page_source))

# 이렇게 하면 진짜 2초를 풀로 기다림.
time.sleep(2)

# 현재 페이지
cur_page=1

# 크롤링 페이지 수
target_crawl_num = 2

# 엑셀 행 수
ins_cnt = 1

while cur_page <= target_crawl_num:

  # bs4 초기화
  soup = BeautifulSoup(browser.page_source, 'html.parser')

  # 소스코드 정리
  # print(soup.prettify())

  # 메인상품 리스트 선택
  prod_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

  # 상품 리스트 확인
  # print(prod_list)

  # 페이지 번호 출력
  print("****** Current Page : {}".format(cur_page), "******")
  print()

  for v in prod_list:
    # print(v)
    if not v.find('div', class_="ad_header"):
      # 상품, 이미지, 가격
      try:
        print(v.select('p.prod_name > a')[0].text.strip())
        prod_name = v.select('p.prod_name > a')[0].text.strip()
        try:
          print('http:'+ v.select('a.thumb_link > img')[0]['data-original'])
          prod_img_url = 'http:'+ v.select('a.thumb_link > img')[0]['data-original']
        except:
          print('http:'+v.select('a.thumb_link > img')[0]['src'])
          prod_img_url = 'http:'+v.select('a.thumb_link > img')[0]['src']

        print(v.select('p.price_sect > a')[0].text.strip())
        prod_price = v.select('p.price_sect > a')[0].text.strip()

        # 이미지 요청 후 바이트 변환
        img_data = BytesIO(req.urlopen(prod_img_url).read())

        # 엑셀 저장(텍스트)
        print('===============variable check===============')
        print(prod_name)
        print('===============variable check===============')
        worksheet.write('A%s' % ins_cnt, prod_name)
        worksheet.write('B%s' % ins_cnt, prod_price)

        # 엑셀 저장(이미지)
        worksheet.insert_image('C%s' % ins_cnt, prod_name, {'image_data': img_data})


        ins_cnt += 1
      except:
        pass

      # 이 부분에서 엑셀 저장(파일, DB 등)
      # CODE
    print()
  print()
  # 페이지 별 스크린샷 저장
  browser.save_screenshot('./resources/target_page{}.png'.format(cur_page))

  # 페이지 증가
  cur_page += 1

  if cur_page > target_crawl_num:
    print('Crawling Succeed')
    break

  # 페이지 이동 클릭
  WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()



  # Beautiful Soup 인스턴스 삭제(안쓰는 객체들은 바로바로 삭제해 주는게 좋음. 위에서 선언한 soup는 더 이상 필요가 없잖아)
  del soup


  # 3초간 대기
  time.sleep(2)



# 브라우저 종료
browser.close()

# 엑셀 파일 닫기
workbook.close()