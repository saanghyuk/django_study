import scrapy

# xpath 선택자 도움 사이트
# https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
# http://www.nextree.co.kr/p6278/

# css 선택자 도움 사이트
# https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors

# 타겟 데이터는 크롬 개발자 도구 사용

# 선택자 연습 팁 : scrapy shell에서 테스트(효율성)
# scrapy shell 도메인

class TestSpider(scrapy.Spider):
    # 스파이더 이름(실행)
    name = 'test5'
    # 허용 도메인
    allowed_domains = ['w3schools.com']
    # 시작 URL(다수 가능)
    start_urls = ['https://www.w3schools.com/']

    # CSS선택자


    def parse(self, response):
        #  둘다 가능
        # xpath일땐?
        # response.css('nav#mySidenav').xpath('./div//a/text()').extract()
        for n, text in enumerate(response.css('nav#mySidenav a::text').getall(), 1): # 1번 index부터 시작
            yield {'num': n, 'learn Title': text}

