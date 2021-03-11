#Section06
#파이썬 함수식 및 람다(lambda)

#함수 정의 방법
#def 함수명(파라미터):
#code

def hello(world):
  print("Hello, ", world)

hello("Python")

def hello_return(world):
  val = 'Hello' + str(world)
  return val

str = hello_return("Python!!")
print(str)


#다중 리턴
def func_mul(x):
  y1 = x*100
  y2 = x*200
  y3 = x*300
  return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

#리스트로 받고 싶은 경우?
def func_mul(x):
  y1 = x*100
  y2 = x*200
  y3 = x*300
  return [y1, y2, y3]

lt = func_mul(100)
print(lt)


#*args, *kwargs
#*이 하나면 tuple, 2개면 dictionary로 넘길 수 있음.

#매개변수에 따라서 함수의 작동을 달리 함. 튜플형태로 넘어옴
def args_function_1(*args): #enumerate는 인덱스를 생성해서 돌려줌
    print(args)
print("args_function_1")
args_function_1('Son')
args_function_1('Kim', 'Son', 'Park')



def args_function(*args):
  for i, t in enumerate(args): #enumerate는 인덱스를 생성해서 돌려줌
    print(i, '번째는', t)

args_function('Son')
args_function('Kim', 'Son', 'Park')


#enumerate
for i, t in enumerate(range(10)):
  print(i, t)


#kwargs, 딕셔너리
def kwargs_function(**kwargs):
  print(kwargs)
  for k, v in kwargs.items():
    print(k, v)

kwargs_function(name1 = 'SON', name2 = 'KIM', name3='PARK')
# kwargs_function('SON', 'KIM', 'YOON') ERROR Becasue there are no key.

#conversion

#아래 함수에는 3번째는 튜플, 4번째는 딕셔너리로 받아서 처리 하겠다는 것.
#*과 **는 가변인자임. 없어도 됨.
def example_mul(arg1, arg2, *args, **kwargs):
  print(arg1, arg2, args, kwargs)

example_mul(10, 20)
example_mul(10, 20, 'park', 'kim', age1=24, age2=35)

# 중첩 함수(closer)
#파이썬 데코레이터, 클로저
def nested_func(num):
  def func_in_func(num):
    print(num)
  print("in func")
  func_in_func(num+10000)

nested_func(10000)


#예제 6 hint! #:int는 들어올 객체를 미리 hint 주는 것. -> list는 나가는 값에 대한 힌트주는 것.
#only for 가독성
def func_mul3(x: int) -> list:
  y1 = x*100
  y2 = x*200
  y3 = x*300
  return [y1, y2, y3]

print(func_mul3(5.0))


#lambda function
#메모리 절약, 가독성 향상, 코드 간결
#함수는 원래는 객체생성 -> 리소스(메모리) 할당
#람다는 즉시 실행함(Heap 초기화)-> 메모리 초기화
#
# 일반적 함수
def mul_10(num : int) -> int:
  return num*10

var_function = mul_10
print(var_function)
print(type(var_function)) #function 이라는 Class로 선언 되어 있음.

print(var_function(10))

#anomyous function
lambda_mul_10 = lambda num : num*10 #num이라는 input을 받아서, x*10이라는 아웃풋을 뱉어
print('lambda >>>>>>', lambda_mul_10(10))

def func_final(x, y, func):ㄴ
  print(x*y*func(10))

func_final(10, 10, lambda_mul_10)
func_final(10, 10, lambda x:x*10000)

