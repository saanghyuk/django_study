# Section02-3
# lxml기초 스크래핑
# css selector : https://www.w3schools.com/cssref/trysel.asp
# pip instal lxml, requests, cssselect

# 문서를 가져와서 parsing(구조에 맞게 내가 가져오는 것, 예. 한글만 가져오기, 특수문자 제거 등).
# 그 중에 많이 사용하는 것이 lxml

import requests
import lxml.html

def main():
  '''
  네이버 메인 뉴스 스탠드 스크래핑 메인함수
  '''

  #스크래핑 대상 URL(앞에서 나온 URLOPEN으로해도 되는데 더 편해서 쓰는 것)
  response = requests.get('https://www.naver.com/') # Get, POST

  # 신문사 링크 리스트 획득
  urls = scrape_news_list_page(response)


def scrape_news_list_page(response):
  # URL LIST 선언
  urls = []
  # 태그 정보 문자열 저장
  # print(response.content)
  root = lxml.html.fromstring(response.content) #<Element html at 0x7fd96ddab228>

  for a in root.cssselect('div._NM_NEWSSTAND_THUMB div.popup_wrap a:nth-child(3)'):
      url = a.get('href')
      print(url)
      urls.append(urls)

  return urls


# 스크래핑 시작
if __name__=='__main__':
  main()
