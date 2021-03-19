# Chapter04-1
# 파이썬 심화
# 일급 함수(일급 객체)

#파이썬 함수 특징
#1. 런타임 초기화
#2. 변수 등에 할당 가능
#3. 함수의 인수로 전달 가능.
#4. 함수 결과로 반환 가능(return funcs)

#함수 객체 예제
def factorial(n):
  '''Factorial Function -> n:int'''
  if n ==1:
    return 1
  return n*factorial(n-1)

class A:
  pass

print('EX1-1 - ', factorial(10))
print('EX1-2 - ', factorial.__doc__)
print('EX1-3 - ', type(factorial), type(A)) # 파이썬의 모든 것은 객체이다.
# print('EX1-4 - ', dir(factorial))
# print('EX1-4 - ', dir(A))
# 1-4로 둘의 차이를 보니깐 딱
# {'__defaults__', '__get__', '__annotations__', '__code__', '__qualname__',
#  '__closure__', '__name__', '__call__', '__globals__', '__kwdefaults__'}
# 이렇게만 나옴.
print('EX1-4 - ', set(sorted(dir(factorial), reverse=True)) - set(sorted(dir(A), reverse=True)))
print('EX1-5 - ', set(dir(A))-set(dir(factorial)))
print('EX1-5 - ', factorial.__name__)
print('EX1-6 - ', factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial
print('EX2-1 - ', var_func)
print('EX2-2 - ', var_func(5))
print('EX2-3 - ', map(var_func, range(1, 6)))
print('EX2-4 - ', list(map(var_func, range(1, 6))))

# 함수의 인수 전달 및 함수로 결과 반환 -> 고위함수(Higher Order Function)
# map(a, b) -> b의 값들을 하나 하나씩 a라는 함수로 통과시켜서 결과를 return
# filter(a, b) -> b의 값들 중에 a의 조건을 충족하는애들만 남겨서 return
print('EX3-1 - ', list(map(var_func, filter(lambda x: x%2, range(1, 6)))))
print('EX3-2 - ', [var_func(i) for i in range(1, 6) if i % 2 ])

# reduce()
from functools import reduce
from operator import add
# reduce함수 정리 https://codepractice.tistory.com/86
# 요즘 잘 안씀
print('EX3-3 - ', reduce(add, range(1, 11))) #뒤에 있는 값을 하나 하나 씩 계속 add해 가는 방식
print('EX3-4 - ', sum(range(1, 11)))


# 익명함수 (lambda)
# 가급적 주석 사용
# 가급적 함수 사용(적재적소에만 사용할 것)
# 일반 함수 형태로 리팩토링 권장.

print('EX3-5 - ', reduce(lambda x, y: x+y, range(1, 11)))
print()
print()


# Callable, 호출 연산자 -> 메소드 형태로 호출 가능한지 확인(__call__의 속성이 있다는 것은 호출이 가능하다는 뜻, function())
import random
#로또 추첨 클래스 선언
class LottoGame:
  def __init__(self):
    self._balls = [n for n in range(1, 46)]


  def pick(self):
    random.shuffle(self._balls)
    return sorted([random.choice(self._balls) for n in range(6)])

  def __call__(self):
    return self.pick()

# 객체 생성
game = LottoGame()

# 게임 실행
print()
print('EX4-1 -', game.pick())

# Callable 확인 이 체크가 된다는 것은 함수처럼 ()사용이 가능하다는 것.
print('EX4-1 -', callable(str), callable(list), callable(factorial), callable(3.14))
print(callable(game)) #이거는 callable 하지가 않음.
#근데 파이썬에서는 game()이렇게 호출할 수 있게 만들 수 있음. __call__
print('EX4-3 - ', game())
print('EX4-3_1 - ', game)

print()
print()


# 다양한 매개변수 입력(*args -> tuple, **kwargs -> dict)
def args_test(name, *contents, point=None, **attrs):
  return '<args_test> -> ({}) ({}) ({}) ({}) '.format(name, contents, point, attrs)

print('EX5-1 -', args_test('test1'))
print('EX5-2 -', args_test('test1', 'test2'))
print('EX5-3 -', args_test('test1', 'test2', 'test3', id='admin'))
# 중간에 튜플이라서 어디까지가 7인지를 알 수가 없잖아. 이런 경우 point는 무조건 이름 넣어줘야지
print('EX5-4 -', args_test('test1', 'test2', 'test3', id='admin', point=7))
print('EX5-4 -', args_test('test1', 'test2', 'test3', id='admin', point=7, password='1234'))


print()
print()


# 함수 Signatures
# 함수의 인자에 대한 정보를 표시해주는 메서드
from inspect import signature

sg = signature(args_test)
print('EX6-1 - ', sg)
print('EX6-2 - ', sg.parameters)

print()

# 모든 정보 출력
for name, param in sg.parameters.items():
  print('EX6-3 -', name, param.kind, param.default)

print()
print()

# partial  사용법 : 인수 고정 -> 주로 특정 인수 고정 후 콜백 함수에 사용하는 함수
# 하나 이상의 인수가 이미 할당된 함수의 새 버전 반환

from operator import mul
from functools import partial

# 10*100도 되는데 왜 굳이 mul을 만들었겠냐?
# 함수를 인수로 쓸 수 있을 것 같으니깐 만든거야.
print('EX7-1 - ', mul(10, 100))
#인수 고정
five = partial(mul, 5)

six = partial(five, 6) # 5로 고정이 되 있는데 6을 또 고정함.

print('EX 7-2 - ', print(five(100)))
print('EX 7-3 - ', print(six()))
print('EX 7-4 -', [five(i) for i in range(1, 11)])
print('EX 7-5 - ', list(map(five, range(1, 11))))
