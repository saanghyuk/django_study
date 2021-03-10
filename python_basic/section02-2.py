# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩

# import this
import sys

# 파이썬 기본 인코딩
# 파이썬은 기본 utf-8
print(sys.stdin.encoding)
print(sys.stdout.encoding)

# 출력문
print("My name is Goodboy!")

# 변수 선언
myName = 'Goodboy'

# 조건문
if myName == 'Goodboy':
    print("OK")


# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)


# 변수 선언 한글로도 가능
이름 = '가나다'
print(이름)

# 함수 선언


def greeting():
    print('Hi, nice to meet you')


# Class
class Cookie:
    pass


# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))
