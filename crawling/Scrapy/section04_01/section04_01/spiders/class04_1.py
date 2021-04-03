import scrapy


class TestSpider(scrapy.Spider):
    name = 'test8'
    allowed_domains = ['computerworld.com/news/']
    start_urls = ['https://www.computerworld.com/news/']

    def parse(self, response):
        """
        :param : response
        :return : Request
        """
        for i, v in enumerate(response.css('div.post-cont h3 > a::text').extract()):
            self.logger.info(v)
            yield dict(num=i, headline=v)

