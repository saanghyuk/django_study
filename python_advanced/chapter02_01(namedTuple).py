# Chapter02-1
# 데이터 모델(Data Model)
# 참조: https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id(주소값), type(자료형) -> value
# 파이썬 -> 굉장히 일관성 있는 언어로 알려짐

# 일반적인 튜플(한번 선언하면 추가는 가능하지만 변하는 것이 불가, 바뀔 일이 없어서 속도가 더 빠름) 사용
# 두 점 사이 거리
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt
line_leng1 = sqrt((pt2[0]-pt1[0])**2 + (pt2[1]-pt1[1])**2)
print('EX1-1', line_leng1)



# 위에서 튜플은 뭐가 x고 뭐가 y인지를 계속 기록하고 봐야됨. 인간이 기억해야 함.
# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언, Class
# Class의 성질, 훨씬 가볍고, 불변의 성질 가지고 있음.
Point = namedtuple('Point', 'x y')

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)
line_leng2 = sqrt((pt2.x-pt1.x)**2 + (pt2.y-pt1.y)**2)
print('EX1-2', line_leng2)
print('EX1-3', line_leng1==line_leng2)

print()

# 네임드 튜플 선언 방법
# 띄어쓰기 이외에도 리스트로 넣어도 됨.
Point0 = namedtuple('Point', 'x y')
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# class 는 예약어이고, 중복은 안됨
# Point4 = namedtuple('Point', 'x y x class')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default = False
print('EX2-1 -', Point1, Point2, Point3, Point4)
#Point4는  Point(x=10, y=20, _2=30, _3=40) 이렇게 바뀌어 있네.

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
print('EX2-2', p1, p2, p3, p4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}
#p5 = Point3(tempt_dict) 그냥 이렇게만 하면, 둘다 통째로 하나로 보는 것
p5 = Point3(**temp_dict)
print(p5)


print()
print()

# 사용
#index로도 사용 가능.
print('EX3-1 -> ', p1[0]+p1[1]) # Index Error 주의
print('EX3-1 -> ', p1.x+p1.y) # class 변수 접근 방식

x, y = p3
print(x, y, x+y)

#Rename 테스트
print('EX3-4-', p4)
print()
print()


#네임드 튜플 메소드
temp = [52, 38]

# _make(): 새로운 객체를 생성
# list to named tuple
p4 = Point1._make(temp)
print('EX4-1-', p4)


# _fields : 필드네임확인
print('EX4-2-', p1._fields, p2._fields, p3._fields)



# _asdict():  OrderedDict로 반환
print('EX4-2 - ', p1._asdict(), p4._asdict())
print(dict(p1._asdict()))

# _replace() 근데 튜플은 불변이라서 새로운 수정된 객체를 반환(id값이 달라짐)
print('EX4-4 - ', p2._replace(y=100))
print(id(p2))
print(id(p2._replace(y=100)))
print()
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반 20명, 4개의 반 -> (A, B, C, D)
# 한 반에 20명

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])
# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]

ranks = 'A B C D'.split()
print(ranks, numbers)
print()
# List Comoprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print('EX5-1 - ', len(students))
print('EX5-2 - ', students)
print('EX5-3 - ', students[4].rank)
print()
print()

# 가독성 안좋은 케이스, LIST COMPREHENSION 너무 길면 가독성이 안좋아짐.
students2 = [Classes(rank, number) for rank in 'A B C D'.split() for number in [str(n) for n in range(1, 21)]]
print('EX6-1 -', len(students2))
print('EX6-1 -', students2)

# 출력
for s in students:
  print('EX7-1 - ', s)
