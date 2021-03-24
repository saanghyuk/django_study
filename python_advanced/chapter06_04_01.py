# Chapter06-04-01
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체의 return을 yield라는 키워드를 통해 사용함(여러 쓰레드를 사용한 효과 내기 위한 기법).
# 실행  STOP  다른작업으로 위임 STOP 이후 그 지점부터 재실행 원리
# Non-Blocking 비동기 처리에 적합.

# Block IO(내가 뭔가 요청을 할때 모든 쓰레드나 루틴들이 멈춰 있는 것, 얘가 일을 끝내야 나머지가 일을 할 수 있는 상황)
# Block IO는 지금까지 사용하던 순차 실행을 의미함.

import timeit
from urllib.request import urlopen

urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://kormat.co.kr', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()

# 순차 실행부
for url in urls :
    print('Start', url)
    # 실제 요청
    text = urlopen(url) #Block 에서는 여기서 요청이 하면 이 요청이 끝나고 응답이 올때까지 그 아랫줄이 실행이 안되는 상황.
    # 여러 코루틴들이 일을 하든 어쩌든 이미 여기서 딱 멈춤. -> BLock I/O라고 함. 파일 쓰고 읽기나, 웹 리퀘스트 던질때 등 많이 일어남.
    # 실제 내용
    # print('Contents', text.read())

    print('Done', url)

# 완료시간 - 시작시간
duration = timeit.default_timer() - start

# 총 실행 시간
print('TOTAL TIME', duration) # 결과 보면, 리스트 순서대로 감.

