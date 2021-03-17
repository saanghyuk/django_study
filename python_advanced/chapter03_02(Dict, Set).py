# Chapter03-2
# 시퀀스형
# 해시테이블 -> 적은 리소스로 많은 데이터를 효율적으로 관린.
# Dict -> key 중복 허용 X, Set -> 중복 허용 X
# 중복 허용하지 않는다는 것은 내부적으로 중복을 검사하고 있다는 것. 이때 hashtable 이라는 것이 사용되는 것.
# 해시 테이블 엔진에서 해시라는 숫자를 만들어서, 그 숫자끼리 비교함.

# Dict  구조
print('EX1-1 - ')
# print(__builtins__.__dict__)
print()
print()

# Hash 값 확인
# tuple은 값을 변경할 수 없는 불변형, list는 값을 변경 가능(Hash값 생성 불가).
t1 = (10, 20, (30, 40, 50))
t2 = [10, 20, [30, 40, 50]]

print('EX1-2 - ', hash(t1)) #이건 고유의 해시를 가지게 됨.
# print(hash(t2)) list는 해시 생성 안함.

print()
print()

# 지능형 딕셔너리(Comprehending Dict)
import csv

# 외부 CSV TO LIST of tuple
with open('./resources/test1.csv', 'r', encoding='UTF-8') as f:
  temp = csv.reader(f)
  #Header Skip
  next(temp)
  #변환
  NA_CODES = [tuple(x) for x in temp]

# print(NA_CODES)

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}
print('EX2-2 - ', n_code1)
print('EX2-3 - ', n_code2)
print()
print()
print()

# Dict Setdefault
source =(
  ('k1', 'val1'),
  ('k1', 'val2'),
  ('k2', 'val3'),
  ('k2', 'val4'),
  ('k2', 'val5')
)
new_dict1 = {}
new_dict2 = {}


# No use Setdefault
for k, v in source:
  if k in new_dict1:
    new_dict1[k].append(v)
  else:
    new_dict1[k] = [v]

print('EX3-1 - ', new_dict1)

# Use Setdefault
# k가 있는지 확인하고, 없으면 []를 넣고 없으면. 그 value값을 반환함.
for k, v in source:
  new_dict2.setdefault(k, []).append(v)
  # print(new_dict2.setdefault(k, []))

print('EX3-2 - ', new_dict2)

# 사용자 정의
# dict를 class로 정의해서 상속해서 사용할 수있음. Userdict가능

class UserDict(dict):
  def __missing__(self, key):
    print('Called : __missing__ ')
    if isinstance(key, str):
      raise KeyError(key)
    return self(str(key))

  def get(self, key, default=None):
    print('Called : __getitem__ ')
    try:
      return self[key]
    except KeyError:
      print(default)
      return default

  def __contains__(self, key):
    print('Called : __contains__ ')
    return key in self.keys() or str(key) in self.keys()

user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2, 1 : 3})
user_dict3 = UserDict([('one', 1), ('two', 2)])

print('EX4-1 -', user_dict1, user_dict2, user_dict3)
print('EX4-2 - ', user_dict2.get('two'))
print('EX4-2-1 - ', user_dict2.get(1))
# print('EX4-3 - ', 'one' in user_dict3)
# # print('EX4-4 - ', user_dict3['three'])
# print('EX4-4 - ', user_dict3.get('three'))
# print('EX4-5 - ', 'three' in user_dict3.get('three'))


print()
print()
# Immutable Dict
# Originally values, keys in dictionary are mutable

from types import MappingProxyType
d = {'key1': 'TEST1'}

# Read Only
d_frozen = MappingProxyType(d)
print('EX5-1 - ', d, id(d))
print('EX5-2 - ', d_frozen, id(d_frozen))
# is는 id비교, ==는 값 비교
print('EX5-3 - ', d is d_frozen, d == d_frozen)

# d_frozen['key1']='TEST2' #immutable

print()
print()
print()

d['key2']='TEST2'
print('EX5-4 - ', d)

# Set 구조(FrozenSet)
# 중복 허용 X
s1 = {'Apple', 'Orange', 'Apple' ,'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple' ,'Orange', 'Kiwi'])
s3 = {3}
s4 = {} #이렇게 놓으면 공집합이 아니라 딕셔너리
s4_1 = set() # 이게 공집합
s5 = frozenset({'Apple', 'Orange', 'Apple' ,'Orange', 'Kiwi'})

# 추가
s1.add('Melon')
print('EX6-1 -', s1, type(s1))

# 추가 불가, 중요한 데이터는 frozenset으로 쓰자.
# s5.add('Melon')

print('EX6-1 -', s1, type(s1))
print('EX6-2 -', s2, type(s2))
print('EX6-3 -', s3, type(s3))
print('EX6-4 -', s4, type(s4))
print('EX6-5 -', s5, type(s5))


# 선언 최적화
print('EX6-5 - ')
a = {5}
b = set([10])
from dis import dis
print(dis('{10}')) # 이렇게 선언하는게 더 빠르다는 것.
  # 1           0 LOAD_CONST               0 (10)
  #             2 BUILD_SET                1
  #             4 RETURN_VALUE
print('EX6-6 - ')
print(dis('set([10])'))
  # 1           0 LOAD_NAME                0 (set)
  #             2 LOAD_CONST               0 (10)
  #             4 BUILD_LIST               1
  #             6 CALL_FUNCTION            1
  #             8 RETURN_VALUE

print()
print()

# 지능형 집합(Comprehending Set)
from unicodedata import name
print('EX7-1 - ')
print({chr(i) for i in range(0, 256)}) #0부터 255까지의 유니코드 데이터
print({name(chr(i), '') for i in range(0, 256)}) #0부터 255까지의 유니코드 데이터 설명
print()
print()
