# Section05-1
# BeautifulSoup
# BeautifulSoup 사용 스크래핑(1) - 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
  <head>
    <title>The Dormoue's story</title>
    <body>
      <h1>this is h1 area</h1>
      <h2>this is h2 area</h2>
      <p class="title"><b>The Dormoue's story</b></p>
      <p class="story">Once upon a time there ware three little sisters
        <a href="http://example.com/elise" class="sister" id="link1">Elsie</a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        <a data-io="link3" href="http://example.com/little" class="sister" id="link3">title</a>
      </p>
      <p class="story">
        story ...
      </p>
    </body>
  </head>
</html>
"""


#예제1 BS4 기초

soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup', type(soup))
print('prettify', soup.prettify()) # 들여쓰기 이런거 알아서 해줌

# h1 태그 접근
h1 = soup.html.body.h1
print('h1', h1)

# p 태그
p1 = soup.html.body.p # p태그가 여러개임. 3개.
print('p1', p1) # 가장 첫번째 것이 나옴.

p2 = p1.next_sibling
print('p2', p2) # 한번만 하면 왜 안나올까? <b>The Dormoue's story</b> 사실 이 부분인데, next_sibling으로 text만 출력은 안해줌.

p2 = p1.next_sibling.next_sibling.next_sibling.next_sibling
print('p2', p2)


# 텍스트 출력 1
print('h1 >> ', h1.string)

# 텍스트 출력 2
print('p >> ', p1.string)

# 함수 확인
# print(dir(p2))

# 다음 엘리먼트 확인
p2 = p1.next_sibling.next_sibling
print('p2', p2)
# print(list(p2.next_element))
print(p2.next_element) # once upon a time there ware three little sisters
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# 이유 from docs: That’s because in the original markup, the word “Tillie” appeared before that semicolon. The parser encountered an <a> tag, then the word “Tillie”, then the closing </a> tag, then the semicolon and rest of the sentence. The semicolon is on the same level as the <a> tag, but the word “Tillie” was encountered first.

# 반복 출력 확인
for v in p2.next_element:
  print(v)


# 예제 2(Find, FindAll)
soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
link1 = soup.find_all('a', limit = 2)
print(type(link1))
print('links', link1)

# link2 = soup.find_all('a', string=["Elsie", 'Title']) #id="link2", string="title", string=["Elsie"] 다 가능
link2 = soup.find_all('a', class_='sister')
print(link2)

for t in link2:
  print(t)


# 처음 발견한 a 태그 선택
link3 = soup.find("a")
print(link3)
print(link3.string)
print(link3.text)

# 다중 조건
link4 = soup.find("a", {"class":"sister", "data-io":"link3"})
print(link4)
print(link4.text)
print(link4.string)

# css선택자 활용: select
# 태그로 접근: find, find_all
# 예제3(select, select_one)
# 태그+클래스+자식선택자
link5 = soup.select_one('p.title > b')
print(link5)
print(link5.string)
print(link5.text)

link6 = soup.select_one("a#link1")
print('link6', link6)
print(link6.string)
print(link6.text)


link7 = soup.select_one("a[data-io = 'link3']")
print('link7', link7)
print(link7.string)
print(link7.text)


# 선택자에 맞는 전체 선택
link8 = soup.select("p.story > a")
print()
print(link8)
print(link8[0].string)


link9 = soup.select('p.story > a:nth-of-type(2)')
print(link9)


link10 = soup.select("p.story")
print()
print("link10")
print(link10)

print("=============")
for t in link10:
  temp = t.find_all("a")

  if temp:
    for v in temp:
      print(">>>>>>", v)
      print(">>>>>>", v.string)

  else:
    print("-----", t)
    print("-----", t.string)







