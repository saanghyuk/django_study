# Chapter02-2
# Python Magic Method
# 참조1 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조2 : https://www.tutorialsteacher.com/python/magic-methods-in-python

# Magic Method
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)

# Magic Method(사용할 수 있게 만들어놓은 집합) Basic
# 파이썬의 모든 자료형은 객체임. Class
# __ __ 로 이루어진 것들을 매직메소드 라고 말함.
# 기본형
print(int)

# 모든 속성 및 메소드 출력
print(dir(int))
print()
print()

n=100

# 사용
print('EX 1-1 - ', n+200)
# 왜 더해질까? 아래처럼 호출이 되는 것.
print('EX 1-2 - ', n.__add__(200))
print('EX 1-3 - ', n.__doc__) # 이것도 개발자들이 이미 int 클래스 정의할 때 넣어 놓은 거지.
print('EX 1-4 - ', n.__bool__(), bool(n))
print('EX 1-5 - ', n.__mul__(100), n*100)

print()
print()

# 클래스 예제 1
class Student:
  def __init__(self, name, height):
    self._name = name
    self._height = height

  def __str__(self):
    return 'Student Class Info : {}, {}'.format(self._name, self._height)

  def __ge__(self, x):
      print('called. >> __ge__ Method.')
      if self._height >= x._height:
        return True
      else:
        return False

  def __le__(self, x):
      print('called. >> __le__ Method.')
      if self._height <= x._height:
        return True
      else:
        return False

  def __sub__(self, x):
    print('called. >> __ge__ Method.')
    return self._height - x._height

s1 = Student('James', 181)
s2 = Student('Mie', 165)

# print(s1 + s2) 지금은 불가능
# 이거는 가능
print(s1._height > s2._height)

# Magic Method Overriding
print('EX2-1 - ', s1 >= s2)
print('EX2-2 - ', s1 <= s2)
print('EX2-3 - ', s1 - s2)
print('EX2-4 - ', s2 - s1)
print('EX2-5 - ', s1)
print('EX2-6 - ', s2)
print()
print()

# 클래스 예제 2
# 벡터 (Vector) #numpy
class Vector(object):
  def __init__(self, *args):
    '''Create a vector, example : v = Vector(1,2)'''
    if len(args)==0:
      self._x, self._Y = 0, 0
    else:
      self._x, self._y = args

  def __repr__(self):
    '''Returns the vector information'''
    return 'Vector(%r, %r)' % (self._x, self._y)

  def __add__(self, other):
    '''Returns the vector addtion of self and other'''
    return Vector(self._x+ other._x, self._y+other._y)

  def __mul__(self, other):
    '''Returns the vector multiply of self and other'''
    return Vector(self._x*other._x, self._y*other._y)

  def __bool__(self):
    return bool(max(self._x, self._y))
# Vector Instance 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector(0, 0)

# Magic Method
print('EX3-1 - ', v1.__init__.__doc__)
print('EX3-2 - ', v1, v2, v3)
print('EX3-3 - ', Vector.__repr__.__doc__)
print('EX3-4 - ', Vector.__add__.__doc__)
print('EX3-5 - ', v1+v2)
print('EX3-6 - ', Vector.__mul__.__doc__)
print('EX3-7 - ', v1*v2)

# print('EX3-8 - ', v2*10)
print('EX3-9 - ', bool(v1), bool(v2))
print('EX3-10 - ', bool(v3))


print()
print()



