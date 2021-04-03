import scrapy
import logging

logger = logging.getLogger("My Logger")

class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'duam.net']
    start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']
    # 실행방법 1
    start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    custom_settings = {
        'DOWNLOAD_DELAY' : 1

    }
    #실행방법 2
    # def start_requests(self):
    #     yield scrapy.Request('http://blog.scrapinghub.com/', self_parse1)
    #     yield scrapy.Request('https://naver.com')
    #     yield scrapy.Request('https://daum.net')

    def parse(self, response):
        self.logger.info(
            'Response URL : %s' %response.url
        )
        self.logger.info(
            'Response Status : %s' %response.status
        )

        if response.url.find('scrapinghub'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
