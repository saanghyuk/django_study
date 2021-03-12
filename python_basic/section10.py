#Section 10
#파이썬 예외처리의 이해
#예외의 종류
#문법적으로 에러는 없지만, 코드실행(런타임) 프로세스에서 발생하는 예외 처리도 중요함.
#linter: 코드 스타일을 알려주고, 문법 체크


#Syntax Error

#print('Test)
#if True
#  pass
#x -> y


#1.Name Error: 참조 변수 없음.
a=10
b=15
#print(c)


#2.ZeroDivisioonError: 0으로 나누기 에러
#print(10/0)


#3. IndexError: 인덱스 범위 오버
x=[10, 20, 30]
#print(x[3])


#4.KeyError
dic = {'Name': 'Son', 'Age' :29, 'City': 'Incheon'}
#print(dic['hobby'])
print(dic.get('hobby'))  #dict쓸때는 get()함수를 쓸 것.

#5.Attribute Error: 모듈, 클래스의 잘못된 속성 사용시의 예외
import time
print(time.time())
# print(time.month())


#6.ValueError: 참조값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10)
# x.index(10)


#7.FileNotFoundError
# f=open('test.txt', 'r')


#8.TypeError:
x=[1, 2]
y=(1, 2)
z='test'

#print(x+y)#서로 다른거끼리 더할 수 없음
#print(x+y)




#항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩.
#그 후 런타임 예외 발생시 예외 처리 코딩 건정(EAFP coding style)
#try: 에러 발생할 가능성이 있는 코드 실행
#except:에러명1
#except: 에러명2
#else: 에러가 발생하지 않았을 경우 실행
#finally: 항상 실행

#Example 1

name = ['Son', 'Lee','Kim']
try:
  z = 'Son'
  x = name.index('Son')
  print('{} Found it! in {} name'.format(z, x+1))
except ValueError:
  print('Not fount it! - Occured Value Error!')
else:
  print('Ok! Else')
finally:
  print('Ok! Finally')

#example2
try:
  z = 'Son'
  x = name.index('Son')
  print('{} Found it! in {} name'.format(z, x+1))
except Exception:
  print('Not fount it! - Occured Value Error!')
else:
  print('Ok! Else')
finally:
  print('Ok! Finally')


#example4
#예외처리는 하지 않지만, 무조건 수행되는 파이썬에서 자주 쓰는 코딩패턴
try:
  print('Try')
finally:
  print('Ok, Finally')


#example5
try:
  z = 'Son'
  x = name.index('Cho')
  print('{} Found it! in {} name'.format(z, x+1))
except ValueError as V1:
  print('Alias')
  print('Not fount it! - Occured Value Error!')
  print(V1)
except IndexError:
  print('Not fount it! - Occured Value Error!')
except Exception:
  print('Not fount it! - Occured Value Error!')
else:
  print('Ok! Else')
finally:
  print('Ok! Finally')


print('-------------------')
#Example6
#raise
#raise 키워드로 예외 직접 발생시킬 수 있음.

try:
  a ='Kim'
  if a =='Kim':
    print('OK, Permit')
  else:
    raise ValueError

except ValueError:
  print('Problem!!!')
except Exception as f:
  print(f)
else:
  print('Ok!')
