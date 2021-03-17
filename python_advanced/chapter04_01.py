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

print('EX3-3 - ', reduce(add, range(1, 11)))
print('EX3-4 - ', sum(range(1, 11)))
