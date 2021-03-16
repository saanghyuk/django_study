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
  for i in temp:
    print(i)
  #변환
  NA_CODES = [tuple(x) for x in temp]

# print(NA_CODES)

