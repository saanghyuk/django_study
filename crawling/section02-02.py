# Section02-02
#Urlopen 함수 기초 사용법
# URLretrieve는 다운로드 까지 함.
# URLOPEN은 웹에서 받은 정보를 가지고 있고, 다른 함수에서 매개변수로 받으면서 사용할 수 있음.


import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ['./resources/test1.jpg', './resources/index.html']

# 다운로드 리소스 url
target_url = ['https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EC%82%AC%EC%9E%90#',
 'https://google.com']

for i, url in enumerate(target_url):
  # 예외 처리
  try:
    # 웹 수신 정보 읽기
    response = req.urlopen(url)

    # 수신 내용
    contents = response.read()

    print('-------------------------------')

    # 상태 정보 중간 출력
    print('Header Info - {} : {}'.format(i, response.info()))
    print('HTTP Status Code : {}'.format(response.getcode())) # status code
    print()
    print('-------------------------------')

    with open(path_list[i], 'wb') as c:
      c.write(contents)

  except HTTPError as e:
    print('Download Failed.')
    print('HttpError Code:', e.code)
  except URLError as e:
    print('Download Failed.')
    print('URL Error Reason : ', e.reason)

  #성공
  else:
    print()
    print('Download Succeed.')
