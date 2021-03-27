# Chapter03-01
# Get 방식 데이터 통신(3) - RSS

# 알립니다 - https://mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001
# 이 뒤 번호가 1002 1003 이렇게 다 다른 게시판 RSS 제공 함.

import urllib.request
import urllib.parse

# 행정안전부 https://mois.go.kr
# 행정안전부 RSS API URL
API = "https://mois.go.kr/gpms/view/jsp/rss/rss.jsp"
params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# 중간 확인
# print(params)

# 연속해서 요청
for c in params:
    # print(c)
    param = urllib.parse.urlencode(c)
    # URL완성
    url = API+'?'+param

    # URL출력
    print("url", url)

    # 요청
    res_data = urllib.request.urlopen(url).read()
    # print(res_data.decode('UTF-8'))

    #수신 후 디코딩
    contents = res_data.decode('UTF-8')
    print(contents)


