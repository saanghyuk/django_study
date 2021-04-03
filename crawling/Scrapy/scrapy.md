

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
  
  