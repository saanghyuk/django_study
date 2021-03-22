# Chapter06-02
# 흐름제어, 병행처리(Concurrency)
# 코루틴(Coroutine)

# 파이썬 위키독스 https://haerakai.tistory.com/m/36

# yield: 메인루틴과 서브루틴과의 통신을 할 수 있게 해줌.
# 코루틴 제어, 코루틴 상태, 양방향 값 전송 가능.
# 메인루틴? 우리가 알던 그 위에서 아래로 가는 흐름. 그러다가 중간에 함수 만나면 실행시키고 리턴 받고 그러는게 서브 루틴. 그러고 다시 메인루틴으로 돌아와서, 실행하지.
# 그 서브루틴을 동시에 여러개 실행시킬 수 있게 해주는게 yield.
# Generator에서 봤듯이 이 구문을 만나면 멈춰있음. 그 다음에 메인 루틴에서 next를 호출 하기 전에는 그 호출된 순간까지 기억하고 있음.
# 코루틴: 코루틴 스케쥴링 오버헤드가 매우 적다(하나의 쓰레드로 신청하기 때문).
# 서브루틴: 메인루틴에서 리턴에 의해 호출 부분으로 돌아와 다시 프로세스를 시작함.
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 수행 가능 -> 동시성 프로그램을 가능하게 해줌.
# 쓰레드 : 지금까지 우리는 싱글 쓰레드 -> 멀티쓰레드는 복잡함 왜냐면, 공유되는 자원에 대한 교착상태 발생 가능성이 있기 때문. 컨텍스트 스위칭 비용 발생, 자원소비 가능성 증가.

# 코루틴 예제
def coroutine1():
  print('>>> coroutine started')
  i = yield
  print('>>> coroutine received : {}'.format(i))

# Generator 선언
c1 = coroutine1()
print('EX1-1 - ', c1, type(c1)) # GENERATOR

# yield 실행 전까지 진행

next(c1) # 임시 주석

# next(c1) #다음 yield가 없는데 next를 호출하면 모든 generator는 error가 남.
# 기본으로 메인루틴이 None을 전달.
# 값 전송

# c1.send(100) 임시 주석


c2 = coroutine1()
# c2.send(100) # 앞부분 next없이 바로 send로 보내면 에러가 남. #TypeError: can't send non-None value to a just-started generator
next(c2) # yield 앞에 멈춰 놔야 값을 받을 수 있음.
# c2.send(100) #여기다 넣으면 실행 잘 됨.


# 코루틴 예제 2
# GEN_CREATED: 처음 대기 상태
# GEN_RUNNING: 실행 상태
# GEN_SUSPENDED : yield대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
  print('>>>>Coroutine Started : {}'.format(x))
  # a = yield
  # print(a)
  y = yield x # y는 메인루틴에서 받을 값, x는 메인루틴으로 전달할 값.
  print('>>>>Coroutine Received : {}'.format(y))
  z = yield x+y
  print('>>>>Coroutine Received : {}'.format(z))

c3 = coroutine2(10)
from inspect import getgeneratorstate

print('EX1-2,', getgeneratorstate(c3)) #GEN_CREATED
print(next(c3)) # send는 대기상태이고, 보낼꺼는 이미 보낸 상태가 됨. 10이 나옴.
print('EX1-3,', getgeneratorstate(c3)) #GEN_SUSPENDED
print(c3.send(15))
print('EX1-4,', getgeneratorstate(c3)) #GEN_SUSPENDED
# print(c3.send(20)) # 예외처리 해야함.

print()
print()

# 근데 무조건 처음에 next()를 호출해야 함.
# 그렇게 해야 값 받는 딱 그 전까지 가서 멈추고 SUSPENDED상태가 됨.
# 처음부터 바로 값 보내면 ERROR

# 데코레이터 패턴
from functools import wraps

def coroutine(func):
  '''Decorator run until yield'''
  @wraps(func) # 주석이나 모든 것까지 다 가지고 가겠다는 데코레이터
  def primer(*args, **kwargs):
    gen = func(*args, **kwargs)
    print(next(gen)) # next 한번 호출하고 보내는 것
    return gen
  return primer

@coroutine
def summer():
  total = 0
  term = 0
  while True:
    term = yield total
    total += term

# Coroutine은 이렇게 담아야 generator로 바뀜. 그냥 하면, generator가 안됨.
su = summer() #이렇게 담기는 순간 클로져가 있으니깐, 내부 prime이 실행된 상태로 return을 받겠지.
# print('EX2-0 - ', next(su))
print('EX2-1 - ', su.send(100))
print('EX2-2 - ', su.send(40))
print('EX2-3 - ', su.send(60))

print()
print()


# 코루틴 예제 3(예외 처리)
# StopIteration을 만들어
class SampleException(Exception):
  '''설명에 사용할 예외 유형'''

def coroutine_except():
  print('>>> coroutine started. ')
  try:
    while True:
      try:
        x = yield
      except SampleException:
        print('-> SampleException handled. Continuing...')
      else:
        print('-> coroutine received : {}'.format(x))
  finally:
    print('-> coroutine ending')

exe_co = coroutine_except()
print('EX3-1 - ', next(exe_co))
print('EX3-2 - ', exe_co.send(10))
print('EX3-3 - ', exe_co.send(100))
print('EX3-4 - ', exe_co.throw(SampleException)) # 예외 던지기
print('EX3-5 - ', exe_co.send(1000))
print('EX3-6 - ', exe_co.send(1000)) # 마지막에 더 이상 안 던질때 알아서 finally를 실행시키네... 신기하네.
print('EX3-7 - ', exe_co.close()) #이제 그만 종료하기 GEN_CLOSED
# print('EX3-8 - ', exe_co.send(1000) # 이제부터 에러

print()
print()

# 코루틴 예제(return)

def averager_re():
  total = 0.0
  cnt = 0
  avg = None
  while True:
    term = yield
    if term is None:
      break
    total += term
    cnt += 1
    avg = total/cnt
  return 'Average : {}'.format(avg)

avger2 = averager_re()
next(avger2)
avger2.send(10)
avger2.send(30)
avger2.send(50)

try:
  avger2.send(None)
except StopIteration as e:
  print('EX4-1 - ', e.value) # 이 에러의 value안에 우리가 return한게 들어서 오네.


# 코루틴 예제 5(yield from)
# Stop Iteration을 자동 처리해줌(3.7부터는 await로 바뀜)
# 중첩 코루틴 처리

def gen1():
  for x in 'AB':
    yield x
  for y in range(1, 4):
    yield y

t1 = gen1()
print('EX5-1 - ', next(t1))
print('EX5-2 - ', next(t1))
print('EX5-3 - ', next(t1))
print('EX5-4 - ', next(t1))
print('EX5-5 - ', next(t1))
# print('EX5-6 - ', next(t1)) # StopIteration

t2 = gen1()
print('EX5-7 - ', list(t2))

print()
print()

# 알아서 제어 해줌.
def gen2():
  yield from 'AB'
  yield from range(1, 4)

t3 = gen2()
print('EX6-1 - ', next(t3))
print('EX6-2 - ', next(t3))
print('EX6-3 - ', next(t3))
print('EX6-4 - ', next(t3))
print('EX6-5 - ', next(t3))
# print('EX6-6 - ', next(t3)) # StopIteration

t4 = gen2()
print('EX6-7 - ', list(t4))


print()
print()

def gen3_sub():
  print('Sub Coroutine')
  x = yield 10
  print('Received : ', str(x))
  x = yield 100
  print('Received : ', str(x))

def gen4_main():
  yield from gen3_sub() # 코루틴 함수끼리의 통신을 yield from 으로 하는 것.


t5 = gen4_main() # yield from 이 알아서 sub routine을 실행시켜주고 제어해줌.
print('EX7-1 - ', next(t5))
print('EX7-1 - ', t5.send(7))
# print('EX7-1 - ', t5.send(77)) STOP ITERATION

# 그래서 실무에서는 main처럼 코루틴을 관리하는 함수를 하나 만들고,
# 그 안에서 여러가지 yield from 으로 불러들이면서 관리하고 사용함.

