# Scrapy settings for section05_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'section05_03'

SPIDER_MODULES = ['section05_03.spiders']
NEWSPIDER_MODULE = 'section05_03.spiders'

# 파이프라인 활성화
# 숫자가 작을수록 우선순위가 높음.
ITEM_PIPELINES={
     'section05_03.pipelines.NewsSpiderPipeline':300,
 }


# # User-agent 설정
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'

# fake-user-agent middleware 사용
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 다운로드 간격
DOWNLOAD_DELAY = 2

# 쿠키 사용
COOKIES_ENABLED = True

# Referer 삽입
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://media.daum.net',
}

# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 한글 쓰기(출력 인코딩)
FEED_EXPORT_ENCODING = 'utf-8'

# 캐시 사용
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
