# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속

# Class ABC(abstract class)

# class 선언
class VectorP_sample(object):
  def __init__(self, x, y):
    self.__x = float(x)
    self.__y = float(y)

  def __iter__(self):
    # 아래 쓴거는 generator야. next호출 하면 x, 그 다음 호출하면 y가 나오라는 뜻.
    # 리스트를 통으로 보낼꺼면 []로 하면 됨.
    return (i for i in (self.__x, self.__y))

# 객체 선언
v_sample = VectorP_sample(20, 40)
#  print('EX1-1', v.__x, v.__y ) 파이썬에서 밑줄 두개를 놓으면, 감춰버림. error터짐.



# _x라고 해놨어. 그리고 생성할때, y가 40보다 큰지 init에서 체크한다음에 self에 넣었어.
# 근데 init에서 다 체크해놨더니 직접 접근이 가능해서 v._y = 10 해버리면?
# init에서 짜놨던게 싹다 무용지물이잖아.
# 심지어 float으로 넣어놨더니, 그것조차도 10이라는 int로 바뀌어버림.
# 은닉에 완전히 동떨어진 것.
# 그래서 init에서 체크하고, self에 할당하는 것은 그렇게 좋지는 않아.

# 그래서 나온 개념이 Getter, Setter
# 밑줄 두개로 해놔도 사실 값을 바꾸는 방법은 많아.
# _ 두개 붙인 후에, Getter, Setter를 활용하면 됨.

class VectorP(object):
  def __init__(self, x, y):
    self.__x = x
    self.__y = y

  def __iter__(self):
    # 아래 쓴거는 generator야. next호출 하면 x, 그 다음 호출하면 y가 나오라는 뜻.
    # 리스트를 통으로 보낼꺼면 []로 하면 됨.
    return (i for i in (self.__x, self.__y))

  @property
  def x(self):
    print('Called Property X')
    return self.__x

  #getter를 먼저 만들어야 함
  @x.setter
  def x(self, v):
    print('Called Property X Setter')
    self.__x = float(v)

  @property
  def y(self):
    print('Called Property Y')
    return self.__y

  #getter를 먼저 만들어야 함
  @x.setter
  def y(self, v):
    print('Called Property Y Setter')
    if v<30 :
      raise ValueError('30 Below is not possible')
    self.__y = float(v)


# Getter, Setter

v = VectorP(20, 40)
# print(v.__x) # 접근 불가
print(v.x) # 접근 가능해짐. 우리는 __로 정의했는데, 접근 가능해짐
v.x = 10
print(v.x)

print(v.y)
# v.y = 20 Error
v.y = 40
print(v.y)

print('EX1-2 -', dir(v), v.__dict__) # ['_VectorP__x', '_VectorP__y', 'x', 'y'] 알아서 이렇게 만들어져 있음.
# dict찍어보면 실제로 변수는 이렇게 저장되어 있는 것을 알 수 있음. 다만, 파이썬에서 자동으로 x로 호출 가능하게 해준거지.
print(v._VectorP__x)
print(v._VectorP__y)
print('EX1-3 - ', v.x, v.y)
# Iter확인. 그대로 돌리면 Generator에서 하나씩 풀리겠지.
for val in v_sample:
  print('EX1-4', val)


# __slot__
# 파이썬 인터프리터에게 통보하는 역할
# 해당 클래스가 가지는 속성을 제한함.
# 파이썬의 모든 인스턴스는 속성을 가지고, __dict__로 dictionary형태로 관리됨.
# 근데 이 dict는 빠른 검색을 위해서 hash값으로 관리되기 때문에, 메모리를 많이 잡아먹음.
# 클래스를 100개 1000개 씩 하면, 그 만큼 딕셔너리가 생성되는 것.
# 그래서 slot을 사용해서 __dict__속성 최적화 -> 다수 객체 생성 시 메모리 사용 공간 대폭 감소.
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 set 형태 사용.


# Data Science에서 많은 데이터를 사용하는 경우 거의 90% 이상 slots를 사용함.
class TestA(object):
  __slots__=('a')

class TestB(object):
  pass

use_slot=TestA()
no_slot=TestB()

print('EX2-1 -', use_slot)
# print('EX2-2 -', use_slot.__dict__) dictionary 안써서 에러 남ㅁ.
print('EX2-1 -', no_slot)
print('EX2-2 -', no_slot.__dict__)

# 메모리 사용량 비교. 20%씩 차이가 남.
import timeit

#측정을 위한 함수 선언
def repeat_outer(obj):
  # 얘도 클로저야 obj.a가 밖에서 계속 저장되겠지.
  def repeat_inner():
    obj.a = 'Test'
    del obj.a

  return repeat_inner

print(min(timeit.repeat(repeat_outer(use_slot), number=100000)))
print(min(timeit.repeat(repeat_outer(no_slot), number=100000)))


print()
print()

# 객체 슬라이싱
class Objects:
  def __init__(self):
    self._numbers = [n for n in range(1, 10000, 3)]

  # 파이썬에에 있는 len을 오버라이딩
  def __len__(self):
    return len(self._numbers)

  def __getitem__(self, idx):
    return self._numbers[idx]

s = Objects()
# print('EX3-1- ', s.__dict__)
print('EX3-2 - ', len(s)) # 위에서 __len__을 안해놨으면 error가 남. 실제로 확인해보면 len이 없어.

# 파이썬의 list class를 까보면 실제로 __len__과 __getitem__이 저렇게 되어 있음.
# 리스트에서 제공하는 것들중 두가지를 오바리이딩 했기 때문에, 이제부터 s[:100], s[3]이런게 가능한 거임.
print('EX3-3 -  ', len(s._numbers)) # 이렇게 했어야겠지.
print('EX3-4 - ', s[:100])
print('EX3-5 - ', s[-1])
print('EX3-6 - ', s[::10])

print()
print()


# 파이썬 추상 클래스(ABC)
# 참고: https://docs.python.org/3/library/collections.abc.html
# 여기 꼭 참고하기! ABC를 쓰려면, 뭘 구현하라고 abstract method에 나와 있는 것.

# 추상클래스를 사용하는 이유
# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 함.
# 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것.

# 폰 -> 걸다, 끊다, 배터리 충전. 이런거는 매우 필수적인거잖아.
# 이렇게 해놓고 아래서 공통적인거를 다 상속받게 하는거야. 갤럭시 s9, v30이런거를 상속받게 하면서 + 특수한 메소드를 추가시키는 것.



# Sequence 상속 받지 않았지만, 자동으로 __iter__, __contain__(in 동작시키는 메서드) 기능 작동시키는 경우
# 파이썬이 __getitem__보고 알아서 iter, contain을 만들어 주는 것.
# 객체 전체를 자동으로 조사해서 -> 시퀀스 프로토콜 작동시킴

class IterTestA():
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)


i1 = IterTestA()

print('EX4-1 -', i1[4])
print('EX4-2 -', i1[4]) # [idx] 제거 후
print('EX4-3 -', 3 in i1[1:10]) # contain을 파이썬이 알아서 만든 것.
# print('EX4-4 -', [i for i in i1[:]]) # iter을 파이썬이 알아서 만든 것.
# print('EX4-5 - ', len(i1) ) # 자동으로 안만들어 주네.

print()
print()

# Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작
# 독스(https://docs.python.org/ko/3/library/collections.abc.html#collections.abc.Reversible)에 있는 표 제일 왼쪽 abc가 추상클래스 이름이고,
# 그 클래스를 상속을 받는 순간 조건 '추상메서드'를 FM대로 구현해야 함.
from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx] # range(1, 50, 2)

    def __len__(self, idx):
      return len(range(1, 50, 2)[idx])
i2 = IterTestB() # TypeError: Can't instantiate abstract class IterTestB with abstract methods __len__

print('EX4-5 -', i2[4])
print('EX4-6 -', i2[4:10]) # [idx] 제거 후
print('EX4-7 -', 3 in i2[1:10]) # contain을 파이썬이 알아서 만든 것.

print()
print()

# 우리가 직접 abc를 만들어 보자.
# 부모는 뽑기 기계
# 자식은 인형뽑기, 음식 뽑기 등등

import abc

class RandomMachine(abc.ABC): # metaclass=abc.ABCMeta(python 3.4 이하)

  #  추상 메서드
  @abc.abstractmethod
  def load(self, iterobj):
    '''Iterable 항목 추가'''

  # 추상 메소드
  @abc.abstractmethod
  def pick(self, iterobj):
    '''무작위 항복 뽑기'''

  # 자식에서 그냥 호출할 수 있는 메서드
  def inspect(self):
    items = []
    while True:
      try:
        items.append(self.pick())
      except LookupError:
        break

      return tuple(sorted(items))

import random

class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box.')

    def __call__(self):
        return self.pick()  # 서브클래스 확인

# 서브 클래스 확인
print('EX5-1 -', issubclass(RandomMachine, CraneMachine))
print('EX5-2 -', issubclass(CraneMachine, RandomMachine))

# 상속 구조 확인
print('EX5-3 -', CraneMachine.__mro__)

cm = CraneMachine(range(1, 100)) #추상 메소드 구현 안하면 에러

print('EX5-4 -', cm._items)
print('EX5-5 -', cm.pick())
print('EX5-6 -', cm()) # callable
print('EX5-7 -', cm.inspect()) # inspect 부모꺼가 실행되겠지.

