### Crawling with Python

_dir(a)로 적용 가능한 함수 생각하면서 공부할 것._

- 크롤링과 스크래핑 차이.

  - <u>크롤링</u>은 웹 크롤러(자동화 봇)가 일정 규칙으로 웹페이지를 브라우징 하는 것. 크롤러(자동화 봇)가 무수히 많은 인터넷 상의 페이지(문서, html)를 수집해서 어떤 사이트에 어떤 정보가 있는지 분류하고 나중에 쉽게 찾아볼 수 있도록 하는 것. 보통은 범위가 큼.
  - <u>스크래핑</u>: 웹 사이트 상에서 원하는 정보를 추출하는 기술. 보통은 범위가 작음
  - <u>파싱</u> 페이지에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출하여 정보로 가공하는 것을 말한다.

- CSS Selector & Xpatch Selector

  - 개발자도구에서 특정 엘리먼트 누르고 Copy누르면, copy selector 와 copy xpath가 나옴.

- 크롤링 사전 주의사항

  - 크롤러로 과부하가 일어날 경우, 법적인 소지가 있을 수 있음.
  - 대상 웹페이지 조건 확인. robots.txt [robot.txt check blog](https://m.blog.naver.com/PostView.nhn?blogId=http-log&logNo=221104827805&proxyReferer=https:%2F%2Fwww.google.com%2F)
  - 크롤러 분류 - 상태유무(혹시 로그인을 해야 볼 수 있는 것은 아닐까? 등), Javascript유무(이런 경우 selenium이나 다른 엔진을 활용해서 해야함)
  - Request 요청 주의할 점 - 서버 부하 고려(스크래핑 하는데, 신문기사를 1초에 100개씩 가져온다면? 네이버에서 반드시 서버 관리자가 알게 되고 불미스러운 일이 있을 수 있음. 사람이 하는 것처럼 해야함). 특정 사이트 밴 당하고 그럴 수 있음. 상대 사이트에 대한 예의를 지킬 것.
  - 콘텐츠 저작권 문제 - 이미지 크롤링 하는 등의 문제에서 자주 있는 문제.
  - 페이지 구조 변경 가능성 숙지 - 다 짜놨더니 좀 하다가 어느 순간 구조 바뀔 수 있음(요즘은 API를 제공 해줌. 유튜브 같은 곳도 정보를 다 API로 전송을 해줌. 이거를 활용 하면, 서버에 부하를 주지도 않고 좋음).

  -

#### 라이브러리 정리

| 라이브러리            | 역할    | Detail                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| lxml                  | parsing | Requests.get 등으로 가져온 response데이터를 root = lxml.html.fromstring(response.content)등으로 인자로 준 후에, .cssselect등으로 찾을 수 있음.                                                                                                                                                                                                                         |
| requests              |         | response = requests.get('https://www.naver.com/') # Get, POST 혹은, session = requests.Session()등으로 데이터를 가져오는 역할.                                                                                                                                                                                                                                         |
| urllib.request        |         | urllib.request.urlretrieve(img_url, save_path1) 등으로 가져온 데이터를 파일로 저장 혹은, respones = urllib.request.urlopen등 데이터 가져와서 변수에 저장.                                                                                                                                                                                                              |
| urllib.parse.urlparse |         | dict 형태로 key:value를 저장해 놓으면, urllib.parse.urlencode(dict)형태로 format=json&password=111 이런식으로 바꿔줘서 parameter로 담아서 보내기 쉽게 만들어줌.                                                                                                                                                                                                        |
| json                  |         | json.loads(res)[key 값]을 넣어서 json으로 res가 전달되는 경우 풀어줌. 실제로, 상대방이 json형태로 넘겼어도 for line in r.iter_lines(decode_unicode=True):의 type출력해보면, str로 나오는 경우가 많음. 이런 경우 json.loads로 하면 dict형태로 타입이 바뀜. 혹은 **단일 레코드**인 경우 r.json() 그냥 이렇게 해도 됨. print(r.json().keys()) 혹은 r.json().values() 가능 |

상세 설명

- 서버가 클라이언트를 식별할때, 쿠키를 많이 활용함. 예를 들어, 24시간 동안 이 창을 열지 않음, 로그인 상태 유지 등등. Application > Cooies에서 확인 가능.
-

#### Urllib

| library                                         | roles                                                                                                                                              |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| urllib.request.urlretrieve(img_url, save_path1) | 가져온 데이터를 파일로 저장                                                                                                                        |
| response = urllib.request.urlopen               | respones = urllib.request.urlopen등 데이터 가져와서 변수에 저장.                                                                                   |
| urllib.parse.quote_plus()                       | base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" quote = rep.quote_plus('호랑이') url=base+quote 이렇게 쿼리 날릴때 사용 |
|                                                 |                                                                                                                                                    |

urllib header정보 초기화 방법

```
# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
#Header정보 삽입
req.install_opener(opener)
```

#### Requests

|                                      |                                                                                                                                                                                                                       |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| requests.get())                      | GET 요청                                                                                                                                                                                                              |
| requests.headers                     | 들어온 headers 정보 확인                                                                                                                                                                                              |
| r.text                               | 들고온 데이터 확인                                                                                                                                                                                                    |
| r.iter_lines(decode_unicode=True)    | 들고온 데이터 iter돌리기                                                                                                                                                                                              |
| r.encoding                           | 들고온 데이터의 인코딩 확인                                                                                                                                                                                           |
| r.raise_for_status()                 | 예외가 나면 에러뜨고 아니면 그대로 통과                                                                                                                                                                               |
| requests.cookies.RequestsCookieJar() | jar = requests.cookies.RequestsCookieJar() <br>jar.set('name', 'niceman', domain ="httpbin.org", path="/cookies")<br>r=s.get('https://httpbin.org/cookies', cookies = jar) 디테일하게 쿠키 정보 넣을때는 이렇게 넣음. |

Rest API ->

#### json

|                       |                                           |
| --------------------- | ----------------------------------------- |
| json.loads()          | json으로 타입 변경                        |
| requests.get().json() | 단일 레코드인 경우 json으로 타입 변경해줌 |
| json.keys()           | json데이터의 key만 return                 |
| json.values()         | json데이터의 values만 return              |

#### BeautifulSoup

| method            | roles                                                                                                                                                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| soup.prettify()   | 들여쓰기 해서 보여줌                                                                                                                                                                                                                                                                             |
| p1.next_sibling   | 특정 태그 찾은 후에 그 다음 sibling(참고로 한번만 쓰면 그 줄 끝에 공백에 걸려서 2번 4번 이런식으로 해봐야함)                                                                                                                                                                                     |
| h1.string         | 내부 스트링을 빼줌                                                                                                                                                                                                                                                                               |
| soup.find_all()   | 선택자 만족하는 전체를 가져다 줌(참고로 limit=2 등의 파라미터를 주면, 순서대로 딱 그만큼만 가져다 줌. 아니면 싹다 리스트로 가져옴). link2 = soup.find*all('a', class*="syster") 이렇게 조건도 줄 수 있음. string=["Elsie", 'Title'])id="link2", string="title" 이런식으로 조건별로 찾을 수 있음. |
| soup.find()       | 처음 발견한 태그 선택. 다중 조건도 가능 link4 = soup.find("a", {"class":"sister", "data-io":"link3"})                                                                                                                                                                                            |
| soup.select_one() | find계열의 경우는 태그로 접근함. 하지만, select계열은 css선택자로 접근. link5 = soup.select_one('p.title > b') 이런식으로 사용 가능. css selector와 동일.                                                                                                                                        |
|                   | **select 예시**: soup.select_one('p.title > b'), soup.select_one("a#link1"), soup.select_one("a[data-io = 'link3']")                                                                                                                                                                             |
| soup.select()     | find_all과 같으나 css선택자로 사용                                                                                                                                                                                                                                                               |

```
<h1>this is h1 area</h1>

<h2>this is h2 area</h2>

	<p class="title"><b>The Dormoue's story</b></p>

	<p class="story">Once upon a time there ware three little sisters

		<a href="http://example.com/elise" class="sister" id="link1">Elisie</a>

		<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>

		<a data-io="link3" href="http://example.com/little" class="sister" id="link3">title</a>
	</p>
	<p class="story">
        story ...
   </p>

위처럼 되어 있는 경우,
`p1 = soup.html.body.p # p태그가 여러개임. 3개.

print('p1', p1) # 가장 첫번째 것이 나옴.

p2 = p1.next_sibling

print('p2', p2) # 한번만 하면 왜 안나올까? The Dormoue's story 사실 이 부분인데, next_sibling으로 text만 출력은 안해줌.

p2 = p1.next_sibling.next_sibling.next_sibling.next_sibling

print('p2', p2)`

p1에서 next_sibling한번 하면 ',\n' 공백부분이 나오는 것.
한번 더하면 그 다음 p전체,
한번 더하면, 두번째 마지막 공백부분 ',\n'
한번 더하면, 그제서야 두번째 p태그가 나오는 것.
```

### Selenium

요즘은 로그인 등에서, 사용자가 정말 직접 키보드 치고 입력을 했는지, 정상적인 브라우져로 접근 했는지 다 체크함. 동적 랜더링은 할 수가 없음. 요즘은 그런데 정말 가끔, 웹브라우져 쓰는 경우 쿠키나 세션까지 보내야되는 경우도 있음. 그런경우 fake_useragent로 보내면 됨.

- selenium webdriver를 다운받아야 함. https://www.selenium.dev/downloads/

```
  # selenium 임포트
  from selenium import webdriver

  # webdriver 설정(Chrome, Firefox 등)
  browser = webdriver.Chrome('./webdriver/chromedriver')
```

| method                                                                                                                                                                                                                                |                                                          roles                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------: |
| browser.implicitly_wait(5)                                                                                                                                                                                                            |                          속도가 조금씩 달라서, 웹드라이버 쓸때는 조금씩 타이밍을 주는게 좋음.                           |
| from selenium.webdriver.support.ui import WebDriverWait.                                                                                                                                                                              |                                                   **하단 따로 설명**                                                    |
| browser.set_window_size(1920, 1280) maximize_window(), minimize_window()                                                                                                                                                              |                                              해당 크기로 브라우저를 열어줌                                              |
| browser.get('https://daum.net')                                                                                                                                                                                                       |                                                       페이지 이동                                                       |
| browser.page_source                                                                                                                                                                                                                   |    페이지 내용 보는 것. 이 상태로 bs4에 넣어서 확인하는 것. 이제부터는 ajax콜까지 싹다 옴. 개발자도구 그대로 긁어옴.    |
| browser.session_id                                                                                                                                                                                                                    | 세션 값 출력. 브라우저 엔진을 가지고 움직이기 때문에, 세션과 쿠키를 다 가지고 있음. 진짜 브라우져를 가지고 접근하는 것. |
| browser.title                                                                                                                                                                                                                         |                                                      페이지 타이틀                                                      |
| browser.current_url                                                                                                                                                                                                                   |                                                   현재 URL을 가져옴.                                                    |
| browser.get_cookie                                                                                                                                                                                                                    |                      현재 쿠키 정보 출력(개발자도구 -> Application -> 해당 사이트 에 있는 쿠키값)                       |
| browser.find_element_by_css_selector("div.inner_search > input.tf_keyword")                                                                                                                                                           |                                                     css로 태그 찾기                                                     |
| element.send_keys('고려화학매트')                                                                                                                                                                                                     |                                                         키 입력                                                         |
| element.submit()                                                                                                                                                                                                                      |                                                     입력한 키 제출                                                      |
| browser.save_screenshot("./resources/website_ch1.jpg") browser.browser.get_screenshot_as_file("./resources/website_ch2.jpg")                                                                                                          |                                                  스크린샷 찍어서 저장                                                   |
| browser.quit()                                                                                                                                                                                                                        |                                                      브라우저 종료                                                      |
| from selenium.webdriver.chrome.options import Options chrome_options = Options() chrome_options.add_argument("--headless") # 브라우져가 실행되지 않음. browser = webdriver.Chrome('./webdriver/chromedriver', options=chrome_options) |                                         브라우져가 실행되지 않음. 헤드리스 옵션                                         |

|

- headless option

```
from selenium.webdriver.chrome.options

import Options  chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우져가 실행되지 않음.
browser = webdriver.Chrome('./webdriver/chromedriver', options=chrome_options)
```

- Explicit wait

```
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()


  브라우저가 3초간 기다린다. 저  xpath가 브라우저에 나타날 때 까지. 3초 까지 기다린다. 그 전에 나타나면 마우스로 클릭을 해! 3초 넘어갈때까지 안되면 에러를 뱉어!


참고로
time.sleep(2)
browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()
이렇게 sleep으로 하면 진짜 2초를 기다려. 파이썬 인터프리터 엔진 전체가 멈춤.
explicit 위의 예에서는 기다리가 되면 바로 클릭함.


```

#### xlsxwriter 엑셀에 쓰는 것을 쉽게 해주는 라이브러리(section06-04.py)

```
pip install xlsxwriter

import xlsxwriter
from io import BytesIO
import urllib.request as req


import xlsxwriter
from io import BytesIO

# 엑셀 처리 선언
workbook =xlsxwriter.Workbook("./resources/crawling_result.xlsx")
# 워크시트
worksheet = workbook.add_worksheet()
# 엑셀 행 수
int_cnt = 1

# 이미지 요청 후 바이트 변환
img_data = BytesIO(req.urlopen(prod_img_url).read())

# 엑셀 저장(텍스트)
print('===============variable check===============')
print(prod_name)
print('===============variable check===============')
worksheet.write('A%s' % ins_cnt, prod_name)
worksheet.write('B%s' % ins_cnt, prod_price)

# 엑셀 저장(이미지)
worksheet.insert_image('C%s' % ins_cnt, prod_name, {'image_data': img_data})

```
