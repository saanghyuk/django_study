
# Section03-03
# 다음 주식정보 가져오기

# 코드로 요청했는지, 브라우져로 요청했는지 다 분간을 하고 403 등의 restrict가 뜸.
# 헤더정보를 파이썬으로 만들어서 다 보내야 정보를 수신할 수 있음.
# 그냥 https://finance.daum.net/ 이거로 요청하면 정보들이 안와.
# ajax콜로 처음에는 프레임이나 일부 정보만 렌더링이 되고, 추가적으로 네트워크로 오는 것. 비동기 통신.
# 개발자도구 network로 가서, 어디 API에서 정보가 오는 건지 별도의 요청을 추측해서 찾아야 함.

# 찾아서 https://finance.daum.net/api/search/ranks?limit=10 이거로 주소창 쳐보면 403 forbidden이 나옴.
# 막아놓은 것. 헤더정보를 직접 편집을 해줘야함.
# 첫번째 finance.daum.net의 header정보에 referer/user-agent같은거를 넣어보면서, 뭘 넘겨줘야 되는건지 찾아봐야 함.

import json # ranks?limit=10이 json파일로 와서 import
import urllib.request as req
from fake_useragent import UserAgent
import csv
# Fake Header정보(가상으로 User-agent생성)
ua = UserAgent()
# print(ua.ie)
# print(ua.msie)
# print(ua.chrome)
# print(ua.safari)
# print(ua.random) # 실행할때마다 다르게


# Header 정보
headers = {
    'User-agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}


# 다음 주식 요청 url
url = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('UTF-8')

# 응답 데이터 확인(Json)
# print(res)


# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(res)['data']

# 중간 확인
print('중간 확인 : ', rank_json,' \n') # 리스트 안에 dict객체들이 들어가 있네

for elm in rank_json:
    # print(type(elm))
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm.get('tradePrice'), elm['name']))


    with open ('stock.csv', 'a') as csvfile:
        fieldnames = ['rank', 'tradePrice', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'rank':elm['rank'], 'tradePrice':elm.get('tradePrice'), 'name': elm['name']})
