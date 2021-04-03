import scrapy

from ..items import ItArticle

class TestSpider(scrapy.Spider):
    name = 'test7'
    allowed_domains = ['computerworld.com/news/']
    start_urls = ['https://www.computerworld.com/news/']

    def parse(self, response):
        """
        :param : response
        :return : Request
        """
        for url in response.css('div.post-cont h3 > a::attr("href")').extract():
            self.logger.info('Response URL : %s' %response.urljoin(url))
            yield scrapy.Request('https://www.computerworld.com'+str(url), self.parse_article, dont_filter=True)


    def parse_article(self, response):
        print(">>>>>>>>>>", response)
        """
        :param : response
        :return : items
        """
        item = ItArticle()
        item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item['img_url']= response.xpath('//figure[@itemprop="image"]/img[@itemprop="contentUrl"]/@data-original').get()
        item['contents'] =''.join(response.xpath('//div[@itemprop="articleBody"]/p/text()').getall())

        print("=======================")
        print(dict(item))
        print("=======================")


        yield item