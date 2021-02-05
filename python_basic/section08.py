#Section08
#파이썬 모듈과 패키지

#패키지 예제
#상대 경로
#.. : 부모 디렉토리
# . : 현재 디렉토리


# Usage 1
from pkg.fibonaccci import Fibonacci

Fibonacci.fib(300)

print('ex2 : ', Fibonacci.fib2(400))
print('ex2 : ', Fibonacci().title) #init 해줘야 instance가 호출되니깐!

#Usage 2, not recommended, memory too much
from pkg.fibonaccci import *


#Usage 3
from pkg.fibonaccci import Fibonacci as fb

fb.fib(1000)

print('ex3 : ', fb.fib2(400))
print('ex3 : ', fb().title) #init 해줘야 instance가 호출되니깐!


#Usage 4
import pkg.calculations as c
print('ex4 : ', c.add(10, 100))
print('ex4 : ', c.mul(10, 100)) #init 해줘야 instance가 호출되니깐!

#Usage 5
from pkg.calculations import div as d
print("ex5 : ", int(d(100, 10)))

#Usage 5
import pkg.prints as p
p.prt1()
p.prt2()


#Basic Package in Python
import builtins
print(dir(builtins))

