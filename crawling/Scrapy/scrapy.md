

- Framework : 만들어져 있는 것을 **사용법** 위주로 배우면 됨. 프레임워크로서 굉장히 편하게 개발 되어 있음. 빠르게 매우 안정적. 성능도 매우 좋음. 
- 크롤링을 본격적으로 배우는 단계. 
- DOCS : https://docs.scrapy.org/en/latest/

```
설치 방법
pip install scrapy
https://docs.scrapy.org/en/latest/intro/install.html 

셋업 툴 업그레이드 
pip install --upgrade setuptools

pip upgrade -> ∞¯≈Î
python -m pip install --upgrade pip
```



- Start Project 

  ```
  # start proejct
  scrapy startproject section01_02
  
  # 기본적으로 프로젝트 시작을 하면 아래와 같은 디렉토리 구조가 생성되어짐. 그 중 이 spider내부에 스파이더를 만들고, 이 스파이더가 크롤링을 해 오는 역할을 함. 
  ```

  <img src="/Users/sanghyuk/Documents/django/crawling/Scrapy/resource/Screen Shot 2021-04-01 at 11.50.26 PM.png" alt="Screen Shot 2021-04-01 at 11.50.26 PM" style="zoom:50%;" />

	```
이제부터 명령어는 그 포르젝트 내부 가서 실행. 
scrapy genspider testspider scrapinghub.com
	genspider -> core spider를 만들어줌
	스파이더 이름 testspider
	크롤링할 url
	
	이제 해당 spiders 폴더 내부 내가 만든 스파이더이름으로 파일이 자동으로 생성됨. 
	```

- 실행방법

  ```
  scrapy crawl test1
  
  # 참고로 scrapy crawl test1 --nolog 로 하면, 로그가 안찍히고 실행함(우리가 print찍은 것만 나옴).
  # test1은 class내부 내가 name으로 지정해놓은 이름. 
  # 친 순간 가서 가져 온 것. 
  ```

  - 다녀온 순간, class 내부 parse함수 response에 정보가 들어오게 됨. 

  ```
  scrapy runspider testspider.py로 해당 위치에 가서 실행해도 같음. 
  ```

  - 보통은 만들면서 단위 테스트는 runspider로, 이후 실제 실행시키면서 정기적으로 작동시킬때는 crawl을 자주 씀. spider여러개가 있고, 하나하나씩 실행시키고 싶을 때는 runspider을 써야 할 수 밖에 없지. 

  ```
  scrapy crawl test2 -o result.jl -t jsonlines
  
  => 참고로 한번 실행이 되면, 해당 파일이 있으면 그 파일 기존 내용 뒤에 추가됨. 
  -o : 파일명 옵션 -> 파일명.확장자
  -t : 파일 형식 옵션 -> json, jsonlines, jl, csv, xml, marshal, pickles
  
  or
  scrapy crawl test2 -o result.csv -t csv
  
  
  부하 걸리지 않게 이거 할때도 settings.py download_delay 잘 조절할것
  ```

  

#### Settings.py

  - DOWNLOAD_DELAY = 1로 change. 3이면 3초에 한번씩 크롤링을 함. 0.2 이렇게 해놓으면 IP가 밴이 당하거나 그럴 수 있음. 간격을 조금 넓게 줘야 서버측에 부하를 안죽. 항상 settings.py가서 DOWNLOAD_DELAY = 1이거 주석 풀고, 1~2초로 해놓는거 습관 들일 것.

  - 동적으로 설정도 가능함. 스파이더 만들때 클래스에 하단처럼 딕셔너리 넣으면 됨.  settings.py랑 값 다르면, 동적으로 설정한게 오버라이딩 되서 우선적으로 작동되게 됨. 

    ```
    custom_settings = {
            'DOWNLOAD_DELAY' : 2,
            COOKIES_ENABLED = False
    
        }
    ```

    



### Methods

| methods         | roles           |
| --------------- | --------------- |
| get()           | 하나만 가져오기 |
| getall()        | 전체 가져오기   |
| extract_first() | 하나 가져오기   |
| extract()       | 전체 가져오기   |
| response.css   | css 찾아오기 response.css('div.oxy-post-wrap a.oxy-post-title::text').getall() |
|response.Xpath|Xpath로 찾아오기. response.Xpath('//div[@class="oxy-post-wrap"]/di/a[@class="oxy-post-title"]/text()')|
|scrapy.Request(data, function)|CallBack|
|response.url.find('scrapinghub')|url에 해당 글자가 들어가있으면 찾아다줌.|
|||

```python
    def parse(self, response):
       
        response.css('div.oxy-post-wrap a.oxy-post-title::text')
				::text -> text 만 뽑아 오라는 것. 

        속성 가져올때는? 
        response.css('div.oxy-post a.oxy-post-image::attr("href")') ::attr("속성이름")
            
    Xpath로 찾아오기. response.Xpath('//div[@class="oxy-post-wrap"]/di/a[@class="oxy-post-title"]/text()')
    response.xpath("//div[@class='post-item']/a/@href")
```



##### parse함수

-   return type: Request, BaseItem, Dictionary, None 중 하나는 반드시 리턴해야 함. 
-   yield는 예약어(참고로 **generator**를 만들지)

```python
 def parse(self, response):
        for text in response.css('div.oxy-post-wrap a.oxy-post-title::text').getall():
            # return type: Request, BaseItem, Dictionary, None
            yield {
                'title' : text
            }

```



### tip

- /visualstudio_1  이런식으로 상대경로가 되어 있다면?

  ```
  response.urljoin(url)
  이렇게 붙여주면, 위에 써있는     start_urls = ['http://blog.scrapinghub.com/']를 보고서 알아서 붙여줌. 
  ```

- Scrapy가 진짜 편한 이유가 

  ```
  import scrapy
  
  
  class Class022Spider(scrapy.Spider):
      name = 'test3'
      allowed_domains = ['blog.scrapinghub.com']
      start_urls = ['http://blog.scrapinghub.com/']
  
      def parse(self, response):
          '''
          :param : response
          :return : Request
          '''
  
          for url in response.css('div.oxy-post a.oxy-post-image::attr("href")').getall():
              # url join이용할 것
              print(response.urljoin(url))
              yield scrapy.Request(response.urljoint(url), self.parse_title)
  
  
  
          for parse_title(self, response):
      				response
              
  ```
  - **parse의 yield부분에 scrapy.Request하면서, 첫번째 인자로 data, 두번째 인자로 함수(self.parse_title)를 줬음. 이러면, 이제 parse_title의 response에 해당 데이터가 담겨서 오는 것.**

  - 위에서 지금 scrapy.Request()하면서 줬으니깐, 10번을 실행을 한 그 결과 데이터가 parse_title로 넘어오는 것. 

  - 콜백 계속 안되는 문제           yield scrapy.Request(response.urljoin(url), callback=self.parse_title, **dont_filter=True**)로 해결함. 



- export 분기 처리 

  ```
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
  
  ```

  

- print로 로그를 찍는 것은 굉장히 안좋음. logger를 사용할 것. 

  ```
  def parse(self, response):
          self.logger.info(
              'Response URL : %s' %response.url
          )
  ```

- 외부 로거도 가져갈 수 있음. 파이썬에 로깅이라는 클래스. 근데 굳이 이럴 필요는 없잖아. 

  ```
  import logging
  
  logger = logging.getLogger("My Logger") # Global Variable
  
  
  로그 찍고 싶은 시점
  logger.info("hi")
  
  
  
  
  ```

  

### Scrapy - Shell

- 테스트 용도로 shell모드를 지원 

- **scrape shell**을 치면, 쉘 모드로 들어감. 

- css나 xpath를 테스트 가능

- 장점 -> 간이 테스트 가능. 예를 들면, 선택자 한번 계속 바꿀때마다,  scrapy crawl test3 이런게 너무 불편하잖아. 

- ```
  # shell 모드 내부
  - scrapy shell
  
  fetch('https://blog.scrapinghub.com') # 데이터 수신 되었음. 
  response
  response body 가능
  
  ```

- ```
  - scrapy shell https://blog.scrapinghub.com
  이제 쉘 모드 내부에서 새로운 것으로 바꾸고 싶으면?
  fetch('https://blog.scrapinghub.com') 다시 하면 됨. 
  
  
  
  # 참고로 robotstxt가 안된다고 되있으면 실행을 안함. 
  그런 경우, settings.py값들을 뒤에서 줄 수 있음.
  scrapy shell https://daum.net --set="ROBOTSTXT_OBEY=False"
  ```

- ``` 
  view(response) -> 지금 들어있게 뭔지 확인하고 싶을떄, 실제 저 사이트가 열리는게 아니라 내 브라우져가 해당 내용을 다운받아서 올려줌. 
  ```

- ```
  dir(response)
  
  이런거 다 가능
  
  response
  response.url로 현재 어디 패치 상태인지 확인해줌. 
  response.body
  response.header
  ```

- 



### Spider

- 스파이더는 종류도 여러가지가 있음. 2, 3, 4번은 보통 딱 그 사이트에서 그거만 긁어오겠다. 딱 맞는 경우 아니면 보통 잘 안씀. 보통은 디폴트 스파이더인 Original스파이더를 많이 씀. 
  - CrawlSpider
  - XMLFeedSpider
  - CSVFeedSpider
  - SitemapSpider
- allowed_domains
| methods         | roles                                                        |
| --------------- | ------------------------------------------------------------ |
| allowed_domains | 안에 적혀있는 도메인들만 허락하겠다.                         |
| start_urls      | 방문하는 사이트 목록. 여러개를 나열하면, 해당 모든 사이트를 다 방문하게 됨. |
|                 |                                                              |



- - **멀티 도메인 실행방법 1**
  ```
    class TestSpider(scrapy.Spider):
      name = 'test4'
      allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'duam.net']
      start_urls = ['http://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']
  ```
  
  - **멀티 도메인 실행방법 2** - 좋은 점은 각각 처리할 함수를 따로 지정할 수 있음. 
  
	```
  
  def start_requests(self):
					yield scrapy.Request('http://blog.scrapinghub.com/', self_parse1)
	        yield scrapy.Request('https://naver.com')
	        yield scrapy.Request('https://daum.net')
	```





### Scrapy  - Selector

- xpath 선택자 도움 사이트
  
  - https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths

  - http://www.nextree.co.kr/p6278/
  
  css 선택자 도움 사이트
  
  - https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors

- get() == extract_first(), 

  getall() == extract()

  

- **CSS 선택자**

  | selector | meanings                                                     |
  | -------- | ------------------------------------------------------------ |
  | A B      | 자손 선택자. 하위에 여러개의 테그가 있어도, 존재만 하면 가지고 오게 됨. |
  | A > B    | 자식 선택자. 바로 하위                                       |
  | ::text   | 노드 텍스트만 추출                                           |
  |::attr(name)|노드 속성값 추출|
  |get(), getall()|get(default="") 사용 가능. 내부가 없을때는 디폴트 값을 줄 수가 있음.)|

  **Example**

  - response.css('title::text').get() => 타이틀 테그 텍스트만 추출 
  - response.css('div > a:attr(href)').getall() -> div 태그 자식 a태그 href 속성 값 전부 추출

-  **Xpath**(테스트 사이트: https://www.easycodeforall.com/generate-xpath.html)
	
  | selector | meanings                                                     |
  | -------- | ------------------------------------------------------------ |
  | nodename | 이름이 nodename을 선택                |
  | text()   | 노드 텍스트만 호출                    |
  | /        | 루트부터 시작                         |
  | //       | 현재 노드부터 문서상의 모든 노드 조회 |
  | .        | 현재 노드                             |
  |..|현재 노드의 부모 노드|
  |@|속성 선택자|
  |extract(), extract_first()사용 숙지||

  
  **Example**
  
  - response.xpath('/div') : 루트 노드부터 모든 div태그 선택
    - response.xpath('//div[@id = "id"]/a/text()') : div 태그 중 id가 "id"인 , 자식 a 태그 텍스트 추출

- 중요!  xpath와 css선택자 혼합 사용도 가능. 

  **Example**

  - response.css('img').css('img').xpath('@src').getall()



- 쉘 실행 -> 선택자 확인 -> 코딩 -> 데이터 저장(프로그램 테스트)





### Scrapy - Items 

- 구조적으로 크롤링이 가능하게 해줌. 지금까지는  yield로 그냥 딕셔너리로 리턴함. 

- 수집할 데이트들은 구조적, 체계적으로 구분할 수 있게 해주는 것이 itemrs. 

- **스파이더는 딱 크롤링만 해주는 코어. 크롤링의 대상이 되는 데이터들은 items에서 관리**.

- 장점
  1. 수집 데이터를 일관성 있게 관리 가능. 
  2. 데이터를 사전형(Dict)로 관리. 오타 방지. 
  3. 추후 가공 및 DB에 저장 용이함.
  
- 사용법

  | 순서                         | 역할 |예시|
  | ---------------------------- | ---- | ---- |
  | 무엇을 가지고 올지 미리 확인 |  |1. 기사 헤드라인, 클릭 한후 상세페이지의 2. 이미지와 3. 본문 내용.|
  | items에 클래스 정의 |      |title = scrapy.Field()<br/>contents = scrapy.Field()<br/>contents = scrapy.Field()|
  | Spider에서 넣고 싶은 곳에서 item클래스 정의 후, 해당 인자로 넣는다. |      |item = ItArticle()<br/>item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()<br/>item['img_url']= response.xpath('//img[@itemprop="contentUrl"]/@src').get()|
  |이후 yield에서 item한번에 내보내면 끝||-o test6.jl 쓰면, 파일 저장됨.|
  ||||

  ```
  items.py
  
  
  import scrapy
  
  
  class ItArticle(scrapy.Item):
      # define the fields for your item here like:
      # name = scrapy.Field()
  
      # 제목
      title = scrapy.Field()
      # 이미지 URL
      contents = scrapy.Field()
      # 본문 내용
      contents = scrapy.Field()
  ```



### Scrapy Export

- 셋팅을 한번에 해놓고, 계속해서 알아서 저장이 되도록 만들 수 있음. 

- 지금까지는

  ```
  scrapy crawl test7 -o test7.jl -t jsonlines 
  이런식이였음. 
  
  사실 이런 약자였음. 
  scrapy crawl test7 --output test7.jl -output-format jsonlines 
  ```

- 출력형식

  - JSON
- JSNO Lines
  
  - CSV
- XML, Picke, Marshal

- 저장위치

  - Local File System - My PC(Hard Disk)
  - FTP - Server
  - S3 - AWS(Amazon)
  - 기본 콘솔 확인

- 방법 2가지 

  1. 커맨드 이용

     (--output or -o), (--output-format, -t)

     옵션 설정 예) --set=FEED_EXPORT_INDENT = 2(2번 탭키 누른 것처럼 들여쓰기 넣으면서 저장)

  2. **Settings.py** 이용

     한번 설정해놓으면 자동으로 저장(파일형식, 위치 등)

     https://docs.scrapy.org/en/latest/topics/feed-exports.html#feeds

     | todo              | example                  |
     | ----------------- | ------------------------ |
     | 파일 이름 및 경로 | FEED_URI = "result.json" |
     | 파일 형식         |FEED_FORMAT ='json'      |
     | 출력 인코딩 | FEED_EXPOORT_ENCODING = 'utf-8' |
     | 기본 들여쓰기 | FEED_EXPORT_INDENT = 2 |
     |||
     |||



### Settings.py

- Scrapy 환경설정

- 실행방법

  1. 커맨드 라인에서 실행

     ```
     scrapy crawl 크롤러명 -s(=--set) <NAME>=<VALUE>
     ```

     

  2. Spider 실행 시 직접 지정 - 인자로 뭘 쓰는 것도 없이 그냥 이렇게 선언만 하면 됨. 

     ```
     Spider Class 내부
     
     custom_settings ={
     	'DOWNLOAD_DELAY': 3
     }
     ```

	3. Settings.py에 지정 -> **추천**
	
	4. 서브 명령어(신경 X)
	
	5. 글로벌 설정 :스파이더에서  scrappy.settings.default_settings을 임포트 해서 동적으로 바꾸면서 쓸때 사용. 많이 쓸일은 없음. 



|Name|Roles|
|----|-----|
|SPIDER_MODULES = ['section04_01.spiders']|스파이더가 어디 있는지. 리스트 형태인 것을 보아, 여러 개를 쓸 수 있음.|
|NEWSPIDER_MODULE = 'section04_01.spiders'|새로 생성하면 어디로 갈지(추측)|
|ROBOTSTXT_OBEY = True|타겟사이트 robots.txt 준수 여부. True면 안된다는거 만났을때, 크롤링 멈춤. False면 그냥 함.|
|CONCURRENT_REQUESTS = 32|병렬 처리. 크롤러 양이 많은 경우, 리퀘스트 32개까지 요청을 해서 요청을 하겠다는 것. 컴퓨터 사양이 좋으면 32로 해도 괜찮음. 주석처리 상태면 16개로 되어 있음.|
|DOWNLOAD_DELAY = 3|딜레이 주고 요청함. 시간을 늘릴수록 안전하나 느림.|
|CONCURRENT_REQUESTS_PER_DOMAIN = 16|웹사이트 도메인 동시 병렬 처리 갯수. 16개 사이트를 동시에 할 수 있다.|
|CONCURRENT_REQUESTS_PER_IP = 16|특정 웹사이트 주소 병렬 처리 갯수(IP로 접근 했을 때)|
|COOKIES_ENABLED = False|쿠키 활성화 여부. 서버에 따라서 쿠키 있는지 확인하는 곳이 있음. True로 놓으면 자동으로 크롤링 엔진이 쿠키를 생성해서 크롤링 함. 403, 404 같은거 뜨면, 쿠키 True로 하고 작동시켜 보면 좋음.|
|TELNETCONSOLE_ENABLED = False|원격 할때 씀|
|DEFAULT_REQUEST_HEADERS = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',   'Accept-Language': 'en' }|기본 리퀘스트 헤더값. 헤더값을 보는 사이트는 여기다가 fake_user_agent 같은 것을 두면 됨.  ** 중요**|
|\#SPIDER_MIDDLEWARES =|미들웨어 사용 여부|
|\#DOWNLOADER_MIDDLEWARES =|특정 다운로드 미들웨어 사용|
|\# Configure item pipelines<br/>ITEM_PIPELINES =|파이프라인 설정|
|HTTPCACHE_ENABLED = True|캐시 사용 여부|
|HTTPCACHE_EXPIRATION_SECS = 30|캐시 유효기간(30초마다 캐시를 초기화하겠다.)|
|HTTPCACHE_DIR = 'httpcache'|캐시의 저장 경로|
| HTTPCACHE_IGNORE_HTTP_CODES = []                             |응답 거부 캐시. 크롤링을 시도했는데,|
|HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'|캐시 스토리지|
- 캐시를 사용하면 동일하게 여러 번 요청시 서버사이드 부하 절감 가능(변동사항 없을 경우)

  캐시 사용하면? 1초 전에 실행하고 또 실행하면 엄청 금방 끝남. 만약, 처음 크롤링 하러 갔다가, 안바뀌었어. 바뀐게 없는데 계속 긁으면 서버 측에도 부담을 줌. 나도 리소스 낭비. 처음에는 가지고 오고, 두번째부터는 캐시를 디짐. 30이면 30초 동안은 캐시를 디짐. 그러다가 30초 지나면, 실질적으로 방문해서 긁음. 캐시 만료를 이 사이트 업데이트 되는 주기 정도로 바꿔놓으면 6000이면 6000초 동안은 캐시를 크롤링 하는거고, 6000초 지나면 그때부터 실질적으로 방문하는 것. 

  다음이나, 네이버메인 이런데는 워낙 자주 바뀌니깐 캐시보다는 다운로드 딜레이를 좀 늘려서 사용하는게 좋음. 

  캐시라는 것을 긁어오는것도 내장되어 있는 캐시 미들웨어가 작동을 하는 것. 

- **오류처리, 자동 재시도 설정(꼭 알아야 되서 따로 빼놓음)**

  | options              | meanings                                                     |
  | -------------------- | ------------------------------------------------------------ |
  | RETRY_ENABLED = True | 정기 점검 등에서 잠깐 안될때가 있음. 다시 재시도를 하게 됨.  |
  | RETRY_TIMES = 2      | 재시도 최대 횟수값. 여기선 최대 2번까지. 그 다음에도 안되면 에러 |
  | RETRY_HTTP_CODES = [500, 502, 503, 504, 408] | 재시도 대상 http코드. 내가 지정한 http code에서만 재시도 하게 할 수 있음. 나머지는 재시도 안함. |
|HTTPERROR_ALLOWED_CODES=[404]|오류 무시 HTTP 상태 코드. 404일때는 에러지만 멈추지 않고 무시하고 계속 진행해라.|
|HTTPERROR_ALLOWED_ALL = True|모든 상태 코드 오류 무시. 이건 사용하면 안됨. 모든 에러가 있어도 개무시하겠다는 것.|

  

  
