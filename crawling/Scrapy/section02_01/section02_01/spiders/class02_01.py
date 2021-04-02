import scrapy


class Class0201Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['https://www.zyte.com/blog/']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        """
        params : response
        return : Title Text
        """

        # 2가지(CSS Selctor, Xpath)
        # css
        # 출력 옵션
        # -o 파일명 확장자
        # for text in response.css('div.oxy-post-wrap a.oxy-post-title::text').getall():
        #     # return type: Request, BaseItem, Dictionary, None
        #     yield {
        #         'title' : text
        #     }

        # yield 두개 있으면 에러나서, 뒤에 주석 처리 해 놓음.

        for i, text in enumerate(response.xpath('//div[@class="oxy-post-wrap"]/div/a[@class="oxy-post-title"]/text()').getall()):
            yield {
                'number': i,
                'title' : text
            }




