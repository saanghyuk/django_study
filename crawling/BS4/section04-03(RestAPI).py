# Section 04-03
# Requst
# Rest API: GET, POST, DELETE, PUT(입력):UPDATE, REPLACE(수정)(FETCH : UPDATE, MODIFY)
# URL을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# GET: /movies : 영화를 전부 조회(url만 보고 서버에 대한 요청을 확인 가능하다는 것)
# GET : /movies/:id : 해당 id 의 영화를 조회
# POST : /movies : 영화를 생성
# PUT: /movies : 영화를 수정
# DELETE : /movies : 영화를 삭제

# url의 주소는 계속 비슷한데, 어떤 통신을 하냐에 따라서 계속 달라짐.

import requests

# 세션활성화
s = requests.Session()ㄴ

# 예제 1
r = s.get('https://api.github.com/events')
# 수신상태 체크
r.raise_for_status() # 예외가 나면 에러뜨고 아니면 그대로 통과
# 출력
# print(r.text) # JSON형태

print()
print()
print()


# 예제 2
# 쿠키설정 - 정석으로 하는 방법
jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'niceman', domain ="httpbin.org", path="/cookies")
# 요청
r = s.get('https://httpbin.org/cookies', cookies = jar)
print(r.text)
print("==============")
print(jar)
print("==============")


# 예제 3
r = s.get('https://github.com', timeout = 5) # 5초 기다렸다가 요청한거 받아옴.

# 출력
# print(r.text)


# 예제 4
r = s.post('http://httpbin.org/post', data={'id':'test77', 'pw':'111'}, cookies = jar)
#출력
print(r.text)
print(r.headers)


# 예제 5
# 요청(POST)
payload1 = {'id':'test77', 'pw':'111'}
payload2 = (('id', 'test77'), ('pw', '111') )
r = s.post('http://httpbin.org/post', data=payload1)
print(r.text)


# 예제 6
# PUT 수정 혹은 삽입
r = s.put('http://httpbin.org/put', data=payload1)
print(r.text)


# 예제 7
# DELETE
r = s.delete('http://httpbin.org/delete', data = {'id': 1})
print(r.text)

r = s.delete('https://jsonplaceholder.typicode.com/posts/1')
print(r.text)
print(r.ok)
print(r.headers)

s.close()

