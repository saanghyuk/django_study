# Chapter06-04-03
# Asyncio

# Reference : https://wikidocs.net/21046

# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체의 return을 yield라는 키워드를 통해 사용함(여러 쓰레드를 사용한 효과 내기 위한 기법).
# 실행  STOP  다른작업으로 위임 STOP 이후 그 지점부터 재실행 원리
# Non-Blocking 비동기 처리에 적합.

# Block IO(내가 뭔가 요청을 할때 모든 쓰레드나 루틴들이 멈춰 있는 것, 얘가 일을 끝내야 나머지가 일을 할 수 있는 상황)
# Block IO는 지금까지 사용하던 순차 실행을 의미함.

# asyncio사용

import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import asyncio
import threading

# aiohttp -> asyncio지원하는 패키지.
# 서로 제어를 양보하면서, 빠르게 동시성 프로그래밍을 활용하는 기법.

urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://kormat.co.kr', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()

# 여러개가 같이 실행되는 함수 앞에 async를 붙임.
async def fetch(url, executer):
  print('ThreadName : ', threading.current_thread().getName(), 'Start', url)
  res = await loop.run_in_executor(executer, urlopen, url) # urlopen은 await이 불가능해서 우회해서 쓰레드로 하게 만든 것.
  print('ThreadName : ', threading.current_thread().getName(), 'Done', url)
  return res.read()[0:5]

async def main():
  # 쓰레드 풀 생성 why? 하단에서 res = await urlopen(url)해놓으니깐, object HTTPResponse can't be used in 'await' expression가 나옴
  # urlopen함수 자체가 예전 함수라서 비동기요청을 하면 막힘.
  # 우리는 항상 async가 붙은 함수를 사용해야 비동기처리가 가능함. urlopen을 따라가보면 내부에 async가 안붙어 있는 것. 그런것만 await 뒤에서 사용 가능.
  # 그래서 쓰레드 사용으로 우회한 것.
  executor = ThreadPoolExecutor(max_workers=10)
  # yield from 이 awiat으로 바뀜
  #asyncio.ensure_future
  futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]
  result = await asyncio.gather(*futures)

  print()
  # 결과 확인
  print('RESULT : ', result)



# 쓰레드는 무조건 진입점이 없으면 에러남
if __name__=='__main__':
  # 루프
  loop = asyncio.get_event_loop() # 중앙 관리를 가져옴
  loop.run_until_complete(main()) # 모든 generator가 끝날때까지 기다려줌.


  # 완료시간 - 시작시간
  duration = timeit.default_timer() - start

  # 총 실행 시간
  print('TOTAL TIME', duration) # 결과 보면, 리스트 순서대로 감.