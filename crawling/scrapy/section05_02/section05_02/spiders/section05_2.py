import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItems
import re



# 링크 크롤링 예제(중요)
# 사이트 요구에 맞는 환경 설정 세팅(중요)
class NewsSpider(CrawlSpider):
    name = 'test12'
    allowed_domains = ['media.daum.net','news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    rules = [
        # page=\d$ or page=\d+$ : 2자리수 페이지 크롤링
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_parent'),
    ]

    def parse_parent(self, response):
        # 부모 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)

        for url in response.css('ul.list_news2.list_allnews > li > div'):
            # 신문기사 URL
            article_url = url.css('strong > a::attr("href")').extract_first().strip()
            # 요청

            # 원하는 데이터 같이 넘기는게 meta, dic으로 보내면 됨.
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url' : response.url}, dont_filter=True)

    def parse_child(self, response):
        # 부모 자식 수신 정보 로깅
        self.logger.info("===============================")
        self.logger.info("Response From Parent URL : %s" % response.meta['parent_url'])
        self.logger.info("Child Response URL : %s" % response.url)
        self.logger.info("Child Response Status : %s" % response.status)
        self.logger.info("===============================")

        pass