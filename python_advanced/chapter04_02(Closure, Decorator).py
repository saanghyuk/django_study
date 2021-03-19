# Chapter04-2
# 파이썬 심화
# 일급함수(일급객체)
# Decorator & Closure

# 파이썬 변수 범위(global)

#예제 1
def func_v1(a):
  print(a)
  print(b)
# func_v1(3) -> 바로 예외. b not defined

#예제 2
b = 10
def func_v2(a):
  print(a)
  print(b)
func_v2(5)


#예제 3
#함수 실행되면서 함수 내부 b는 찾았어. 근데 할당되기 이전이야.
#그러면 global을 찾기 이전에 error을 터뜨림.
#**같은 변수가 있으면 지역 변수가 우선! 지역 변수 내부 값이 있으면, 할당 유무 따짐. **
#**아예 지역 변수가 존재 자체를 안하면, 그때 global을 찾는 것 **
b = 10
def func_v3(a):
  print(a)
  print(b)
  b = 5
# func_v3(5) # UnboundLocalError: local variable 'b' referenced before assignment

from dis import dis
print('EX1-1 - ')
print(dis(func_v3))


print()
print()

# 클로져(Closure)
# 반환되는 내부 함수에 대해서 선언된 연결된 정보 가지고, 참조하는 방식
# 반환 당시 함수의 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능.
a = 10
print('EX2-1 - ', a+10)
print('EX2-1 - ', a+100)

#결과를 누적시킬 수 있을까? reduce나 sum함수들 처럼 가능 하겠지.
print('EX2- 3 - ', sum(range(1, 51)))
from functools import reduce
from operator import add
print(reduce(add, range(51, 101)))
print()
print()
# 근데 class 형태로 만들어 보자는 것.
# 클래스 이용
class Averager():
  def __init__(self):
    self._series = []

  def __call__(self, v):
    self._series.append(v)
    print('class >>> {} / {}'.format(self._series, len(self._series)))
    return sum(self._series) / len(self._series)

# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print('EX3-1 -', avg_cls(10))
print('EX3-2 -', avg_cls(35))
print('EX3-3 -', avg_cls(40))

print()
print()
# 클로저 Closure 사용
# closure_avg1()를 실행하면, averager이 함수를 리턴함.

def closure_avg1():
  # 파이썬은 외부 함수와 내부 함수 사이 공간을 free variabl e영역이라고 말함.
  # 클로져 영역임.
  series = []
  def averager(v):
    # series = [] 이렇게 놨으면 변수 유지가 안됨. 실행시 마다 무조건 []안에 1개가 들어있음.
    series.append(v)
    print('def 1 >>> {} / {}'.format(series, len(series)))
    return sum(series) / len(series)

  return averager

avg_closure1 = closure_avg1() # 함수가 리턴
# 리턴된 함수의 영역에는 series가 없는데 계속 series = []를 참조를 하고 있음. 뭐지?
# 함수 실행이 끝나면, 원래는 소멸되잖아.
# 반환 당시 함수(averager)의 유효범위를 벗어난 변수 또는 메소드(series)에 직접 접근이 가능.
# 내 범위 바깥에 있는 것을 스냅샷 딱 찍어 놓고, 계속 물고 다니면서 사용함.
# 전역변수 사용 줄일 수 있고, 은닉화 가능, 각종 디자인 패턴에도 적용이 가능함.
# 함수형 프로그램에서 자주 활용함.
# 그런데 많이 사용할 경우에는, 함수의 실행이 끝나고 계속 들고 있으니깐 오히려 resource를 너무 과하게 잡아먹지 않게 조심해야 함.
print('EX4-1 -', avg_closure1(15))
print('EX4-2 -', avg_closure1(35))
print('EX4-3 -', avg_closure1(40))

print()
print()


print('EX5-1 - ', dir(avg_closure1))

print()
print('EX5-2 - ', dir(avg_closure1.__code__)) # co_freevars가 있네?
print()
print('EX5-3 - ', avg_closure1.__code__.co_freevars) # 클로져 변수 series가 딱 나옴


print('EX5-4 - ', dir(avg_closure1.__closure__[0]))
print('EX5-4 - ', dir(avg_closure1.__closure__[0].cell_contents))

print()
print()

# closuere 잘못 사용한 경우 벌어지는 일들.
def closure_avg2():
  #Free Variable
  cnt = 0
  total = 0
  def averager(v):
    nonlocal cnt, total
    cnt += 1
    total += v
    print('def 2 >>> {} / {}'.format(total, cnt))
    return total/cnt

  return averager

avg_closure2 = closure_avg2()

print('EX5-5 - ', avg_closure2(15))
# 위는 왜 에러가 날까?
# cnt+=1 에서 cnt가 없으니깐 값을 할당할 수가 없는 거야.
# 기본적으로 내부 함수는 cnt를 보고 내부에서 찾아. 근데 없으니깐 에러를 내는 것.
# 알려줘야돼. 내부 cnt와 외부 cnt가 같다는 것을. 그게 nonlocal cnt, total 이 예약어
# 근데 위에서 list.append는 왜 되는거지?
print('EX5-6 - ', avg_closure2(15))
print('EX5-7 - ', avg_closure2(15))

# func.__closure__ 형태로 자유 변수에 해당하는 객체들을 확인할 수 있고,
# func.__code__.co_freevars 를 통해 자유 변수들의 이름을 확인할 수 있다.



# 데코레이터 실습
# 1. 중복 제거, 코드 간결
# 2. 클로저보다 문법 간결
# 3. 조합해서 사용 용이
#
# 단점
# 1. 디버깅 어려움.
# 2. 에러의 모호함.
# 3. 에러 발생지점 추적 어려움. -> IDE의 도움을 받으면 됨.

import time
def perf_clock(func):
  #closure area
  def perf_clocked(*args):
    # 시작시간
    st = time.perf_counter()
    result = func(*args)
    # 종료시간
    et = time.perf_counter() - st
    # 함수명
    name = func.__name__
    # 매개변수
    arg_str = ','.join(repr(arg) for arg in args)
    # 출력
    print('Result : [%0.5fs] %s(%s) -> %r' % (et, name, arg_str, result))

    return result

  return perf_clocked


@perf_clock
def time_func(seconds):
  time.sleep(seconds)
@perf_clock
def sum_func(*numbers):
  return sum(numbers)
@perf_clock
def fact_func(n):
  return 1 if n<2 else n*fact_func(n-1)


# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

 #이걸 확인하는 이유는, 인자로 들어온 값도 자유 변수니깐.
print('EX7-1 -', non_deco1, non_deco1.__code__.co_freevars)
print('EX7-2 -', non_deco2, non_deco1.__code__.co_freevars)
print('EX7-3 -', non_deco3, non_deco1.__code__.co_freevars)

print('*'*40, 'Called Non Deco ->  time_function')
print('EX7-4 -'),
non_deco1(2)

print('EX7-5 -'),
non_deco2(100, 200, 300)


print('EX7-6 -'),
non_deco3(5)

print()
print()
print()

# 데코레이터 사용
print('*'*40, 'Called Non Deco ->  time_function')
print('EX7-7 - ')
time_func(2)

print('*'*40, 'Called Non Deco ->  time_function')
print('EX7-8 - ')
sum_func(10, 20, 30, 40)

print('*'*40, 'Called Non Deco ->  time_function')
print('EX7-9 - ')
fact_func(100)





