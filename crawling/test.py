# Section05-02
# BeautifulSoup - Image Download

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-agent', UserAgent().ie)]
#Header정보 삽입
req.install_opener(opener)



# 네이버 이미지 기본 URL(크롬 개발자 도구)
base="https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
#검색어
quote = rep.quote_plus('호랑이')
print(quote)
# URL완성
url = base+quote

# 요청 URL확인
print("Request URL : {}".format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = "./resources/image_down"

# 폴더 생성 예외처리(문제 발생 시 프로그램 종료)
try:
  # 기본 폴더 있는지 체크
  if not (os.path.isdir(savePath)):
    # 없으면 폴더 생성
    os.makedirs(os.path.join(savePath))
except OSError as e:
    print("folder creation failed.")
    print("folder name : {}".format(e.filename))

    # 런타임 에러
    raise RuntimeError("System 종료 됩니다")
else:
  # 생성이 되었거나 존재하는 경우
  print('folder is created!')



# bs4 초기화
soup = BeautifulSoup(res, "html.parser")

# print(soup.prettify())



img_list = soup.find_all("img", class_='_image')
print("img")
print(img_list)

for i, img in enumerate(img_list, 1):
  # print(img[src], i)

  # 저장 파일 명 및 경로
  fullFileName = os.path.join(savePath, savePath+str(i)+'.png')
  print(fullFileName)

  # 다운로드 요청(URL, 다운로드 경로)
  req.urlretrieve(img['src'], fullFileName)

# 다운로드 완료시 출력
print('download succeeded')
