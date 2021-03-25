# Section02-01
# urllib 사용법 및 기본 스크래핑

import urllib.request as req

# 파일 url
img_url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4#'
html_url  = 'https://google.com'

# 다운받을 경로
save_path1 = './resources/test1.jpg'
save_path2 = './resources/index.html'

# 예외처리
# 항상 뭔가를 받으면 Headers가 있음.
# http 통신은 한번 요청과 수신 하면 연결 끊김. 그래서 쿠키를 이용해서 세션을 유지시킴
try:
  # urlretrieve 는 다운로드를 받는 함수
  file1, header1 = req.urlretrieve(img_url, save_path1)
  file2, header2 = req.urlretrieve(html_url, save_path2)

except Exception as e:
  print('Download failed')
  print(e)
else:
  # Header 정보 출력
  print(header1)
  print(header2)
  print('Filename 1 {}'.format(file1))
  print('Filename 2 {}'.format(file2))
  print('Download Success')

# 타겟 url에서 내가 원하는 정보 가져오는 것이 시작.
# 그 중에 내가 원하는 정보 찾는 것을 파싱이라 함.



