import scrapy


class TestSpider(scrapy.Spider):
    # 페이지 순회 크롤링 예제
    name = 'test3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    # 메인 페이지 순회
    def parse(self, response):
        """
        :param : response
        :return: Request
        """
        # response.css('div.post-item > div > a::attr("href")').getall()
        # response.css('div.post-item > div > a::attr("href")').extract()
        # response.xpath('//div[@class="post-item"]/div/a/@href').getall()
        # response.xpath('//div[@class="post-item"]/div/a/@href').extract()

        for url in response.css('div.oxy-post a.oxy-post-image::attr("href")').getall():
            # url 보다 urljoin 사용
            print(response.urljoin(url))
            yield scrapy.Request(response.urljoin(url), callback=self.parse_title, dont_filter=True)

    # 상세 페이지 순회
    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param response:
        :return Contents Text :
        """
        contents = response.css('div.ct-text-block > span.ct-span.oxy-stock-content-styles > p::text').extract()[:5]
        # print(contents)
        yield {'contents': ''.join(contents)}
