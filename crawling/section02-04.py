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

    # 결과 출력
    for name, url in urls.items():
      print(name, url)


def scrape_news_list_page(response):
    urls = dict()
    root = fromstring(response.content)
    # # 아무것도 안가져옴
    # for a in root.xpath('//a[text()="기사보기"]'):
    #     print(a.get('href'))
    #     # a 문자열 출력



    # for b in root.xpath('//img[@class="news_logo"]'):
    #     print(b.get('alt'))
    #     # a 문자열 출력

    for a in root.xpath('//div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]'):
        # print(tostring(a, pretty_print=True))
        name, link = extract_contents(a)
        # print('name', name)
        # print('link', link)
        urls[name]= link

    return urls



def extract_contents(dom):
    # dom 구조 확인

    # 신문사 명`
    name = dom.xpath('./a/img/@alt')[0]

    # 링크 주소
    link = dom.xpath('./div/a[text()="기사보기"]/@href')[0]

    return name, link




#  스크랩핑 시작
if __name__ == '__main__':
    main()
