# Chapter03-01
# Get 방식 데이터 통신(1)
# Requests 사용했었는데, 다시 urllib으로 가서 이해해보자.

import urllib.request
from urllib.parse import urlparse


# 기본 요청1(encar)
url = "http://www.encar.com"

# 다운로드 받지 않고 수신된 정보를 변수에 저장
mem = urllib.request.urlopen(url)

# 여러 정보
print('type: {}'.format(type(mem))) # <class 'http.client.HTTPResponse'>
print('geturl : {}'.format(mem.geturl())) # http://www.encar.com/index.do
print('status : {}'.format(mem.status)) # 200
print('headers : {}'.format(mem.getheaders())) # headers:[('CONTENTS HERE')] 참고로 https는 연결 후에 바로 끊기 때문에 ('Connection', 'close') 이렇게 나옴
print('getcode : {}'.format(mem.getcode())) # 200
print('read : {}'.format(mem.read(100).decode('utf-8'))) # 100byte만 읽어옴 그냥 read는 전체 다읽어옴
print('parse : {}'.format(urlparse('http://encar.co.kr?test=test'))) # ParseResult(scheme='http', netloc='encar.co.kr', path='', params='', query='test=test', fragment='')
print('parse query: {}'.format(urlparse('http://encar.co.kr?test=test&pw=111').query)) # test=test

# 기본 요청2(ipify) 쿼리 보내면 다시 보내주는 테스트 사이트
API = "https://api.ipify.org"

# GET 방식 Parameter

# format  jsonp, json, text다 가능 확인해보기
values = {
    'format':'json',
}
print('before param : {}'.format(values))
params = urllib.parse.urlencode(values) #parse가 바꿔 주는 것
print('after param : {}'.format(params))

# 요청 url생성
URL = API+"?"+params
print('요청 URL = {}'.format(URL))

# 수신데이터 읽기
data = urllib.request.urlopen(URL).read()

# 수신데이터 디코딩
text = data.decode('UTF-8')
print('raw data : {}'.format(data))
print('response : {}'.format(text))


