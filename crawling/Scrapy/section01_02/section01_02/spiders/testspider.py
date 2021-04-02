import scrapy


class TestSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['https://www.zyte.com/', 'daum.net']
    start_urls = ['https://www.zyte.com/', 'daum.net'] # 여러개 리스트 형태로도 지정 가능.

    def parse(self, response):
        # print(response)

        print('dir', dir(response))

        print('status', response.status)

        print('text', response.body)
