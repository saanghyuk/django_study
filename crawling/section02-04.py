# Section02-4
# 파이썬 크롤링 기초
# lxml 사용 기초 스크랩핑(2)

import requests
from lxml.html import fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인 함수
    """
    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL
    response = session.get('http://www.naver.com/')
    # 신문사 정보 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)


def scrape_news_list_page(response):
    root = fromstring(response.content)
    #아무것도 안가져옴
    for a in root.xpath('//div[@class="thumb_area"]/div[@class="thumb_box"]'):
        print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

    return



#  스크랩핑 시작
if __name__ == '__main__':
    main()
