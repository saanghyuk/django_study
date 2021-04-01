# Section 04-01
# Requests
# Requests 사용 스크래핑(1) - Session

import requests

# 세션 활성화
a = requests.Session()
r = a.get('https://www.naver.com')

# 수신데이터
# print(r.text)

#  수신상태
print('Status Code: {}'.format(r.status_code))

# 확인
print('OK? : {}'.format(r.ok)) # True or False



# 세션 종료(뒤에 코드 더 있는경우 불필요한 리소스 낭비 막아줌)
a.close()



# 쿠키 return
# https://httpbin.org/ Test 용 페이지
s = requests.Session()

#  쿠키 Return
r1 = s.get('https://httpbin.org/cookies', cookies = {'name':'Son'})
print(r1.text) #  서버가 확인하고 바로 내려줌.


r2 = s.get('https://httpbin.org/cookies/set', cookies = {'name':'Son2'})
print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent':'nice-man_1.0.0_win10_ram16_home_chrome'}

# 헤더 정보 전송
r3 = s.get(url, headers=headers, cookies = {'name':'Son'})
print('headers ========', r3.text)

# 세션 비활성화
s.close()


# 실무에서 with 권장 -> 파일, DB, HTTP통신 등은 with 쓸 것.
with requests.Session() as s:
    r = r.get('https://daum.net')
    print(r.text)
    print(r.ok)
