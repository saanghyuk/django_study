# Chapter 05-1
# 객체 참조 중요한 특징들
# Python Object Reference

print('EX1-1 - ')
print(dir()) #이 파일 자체의 dir

# id vs __eq__(==) 증명
x = {'name': 'kim', 'age':33, 'city':'Seoul'}
y = x

print('EX2-1 -', id(x), id(y)) # id값 같음. 얕은 복사
print('EX2-2 -', x==y) #값이 같냐?
print('EX2-3 -', x is y) # id가 같냐?
print('EX2-4 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y) #x랑 y중 어디에 넣든 둘다 똑같이 추가됨.

print()
print()

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성) 비교, ==(__eq__)는 값을 비교
# tip dict안에 한 100만개 있는데, ==로 값 비교부터 하면? 오래 걸리겠지. 일단은 id가 같을 수도 있으니깐 is로 먼저 비교해보는게 좋겠지.
# __eq__는 ==와 완전 같음.
z = {'name': 'kim', 'age':33, 'city':'Seoul', 'class':10}
print('EX2-6 -', x, z)
print('EX2-6 -', x == z) # True
print('EX2-7 -', x is z) # False
print('EX2-7 -', x is not z) # True

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])
print('EX3-1 -', id(tuple1), id(tuple2)) # 당연히 id는 다르지
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2))
print('EX3-5', tuple1[2] is tuple2[2]) # 내부 리스트의 id값도 다름.

print()
print()

# Copy, DeepCopy(깊은 복사, 얕은 복사)

#copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)
print(id(tl1))
print(id(tl2))
print(id(tl3)) # 얘만 id값 다름.


print('EX4-1', tl1 == tl2) # True
print('EX4-2', tl1 is tl2) # True
print('EX4-1', tl1 == tl3) # True
print('EX4-2', tl1 is tl3) # False, list객체 생성자만 넣었는데 id가 다르네.
# 즉 생성자를 넣어줘야 안전하다는 것.

# 증명
print(id(tl1[1]))
print(id(tl3[1])) # 외부 전체 리스트의 아이디는 달라도, 내부 리스트의 아이디는 같음.
tl1.append(1000)
tl1[1].remove(105)
# 근데 remove하니깐 tl3도 같이 없어지네.
# 왜냐면, 전체 리스트 자체의 id는 tl1, tl3가 서로 다른데, 그 안에 있는 nested 리스트의 아이디 값은 같음.
print(id(tl1[1]))
print(id(tl3[1]))


print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()

tl1[1]+=[110, 120]
tl1[2]+=(110, 120)

print('EX4-8 -', tl1, id(tl1), id(tl1[1]), id(tl1[2]))
print('EX4-9 -', tl2, id(tl2), id(tl2[1]), id(tl1[2])) #여기서는 객체가 재할당(새로 생성) why? because tuple is immutable. 바뀌지 전후 아이디값 확인해 보면 알 수있음.
print('EX4-10 -', tl3, id(tl3), id(tl3[1]), id(tl3[2]))


print()
print()

# Deep Copy
# 장바구니에 담아놓고 결제 할때 잘못 구현하면?
class Basket:
  def __init__(self, products=None):
    if products is None:
      self._products = []
    else:
      self._products=list(products) # 아이디 새로 할당하는 것.

  def put_prod(self, prod_name):
    self._products.append(prod_name)

  def del_prod(self, prod_name):
    self._products.remove(prod_name)

import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)
print('EX5-1 -', id(basket1), id(basket2), id(basket3)) # 객체 복사하니깐 copy든 deep copy든 다 id가 다르게 나옴.
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products)) #얘는 1, 2가 똑같이 나오고 3은 다름.
# 즉 얕은 copy는 객체는 다르게 복사된것 같아도 내부의 attribute들이 똑같이 복사가 된거야.
# deep copy는 내부 attributes까지 다르게 복사되는 것.
# deep copy는 끝까지 쫓아가서 깊게 복사하는 것.

print()
basket1.put_prod('Oranage')
basket2.del_prod('Snack')
print('EX5-3 -', basket1._products) # 똑같이 변경해버렸음.
print('EX5-4 -', basket2._products) # 똑같이 변경해버렸음.
print('EX5-5 -', basket3._products)


print()
print()

# 함수 매개변수 전달 사용법

def mul(x, y):
  x += y
  return x

x=5
y=10
# x랑 y가 함수에 들어갔다가 나와도 당연히 x, y 는 원본이 유지됨.
print('EX6-1 - ', mul(x, y), x, y)

a = [10, 100]
b = [5, 10]

# 리스트를 함수로 넘겼더니, 같이 수정되 버리네. 주소를 넘겼나봄. 가변형일때는 a 데이터가 변형됨.
# 주소를 넘기고 있는 거라는 소리
print('EX6-2 ', mul(a, b), a, b)


c = (10, 100)
d = (5, 10)
print('EX6-2 ', mul(c, d), c, d) # 튜플은 c가 변형이 안됨. # 튜플은 불변형.


# 파이썬 불변형 예외
# str, bytes, frozenset, Tuple: 사본생성 X -> 참조 반환
# 이 예외들은 값이 같으면, id값도 같음.
# 어떻게 복사를 하든 성능을 위해서 id값 통일.
tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1) # 이렇게 하면 원래는 id값이 바뀌는데 안바뀌고 참조를 반환하네.
tt3 = tt1[:]

print('EX7-1 - ', tt1 is tt2, id(tt1), id(tt2)) # True, id값 같음
print('EX7-2 - ', tt1 is tt3, id(tt1), id(tt3)) # True, id값 같음

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 - ', tt4 is tt5, tt4==tt5, id(tt4), id(tt5)) # 얘는 id 다름.
print('EX7-4 - ', ss1 is ss2, ss1==ss2, id(ss1), id(ss2)) #얘는 all true
