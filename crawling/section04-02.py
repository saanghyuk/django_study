# Section 04-02
# Request

# Json : 데이터를 교환하는 방식. 언어와 상관없이 json을 핸들링할수 있는 라이브러리를 대부분 제공함.

import json
import requests

s = requests.Session()

# 100개 JSON 요청
r = s.get('https://httpbin.org/stream/100', stream = True)

# 수신확인
print(r.text)

# 인코딩 Encoding 확인
print('Before Encoding : {}'.format(r.encoding))

if r.encoding is None:
    r.encoding = 'UTF-8'

print('After Encoding : {}'.format(r.encoding))


for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    print(line)
    # print(type(line)) # 문자열로 되어 있음. dict형태로 바꿔줘야 함.

    # JSON(Dict) 변환 후 확인
    b = json.loads(line) # str -> dict
    print(b)
    print(type(b))

    for k, v in b.items():
        print('KEY : {}, VALUE : {}'.format(k, v))

    print()
    print()

s.close()


# https://jsonplaceholder.typicode.com/ 이거 실습

r = s.get('https://jsonplaceholder.typicode.com/todos/1')

# Header정보
print(r.headers)

# 본문 정보
print(r.text)

# json변환
print(r.json())
print(r.json().keys())
print(r.json().values())so

# 인코딩
print(r.encoding)

# 바이너리 정보
print(r.content)

r.close()