# Chapter 03-1
# 파이썬 심화
# 시퀀스 형
# 컨테이너(Container): 서로 다른 자료형을 저장할 수 있음. -> [list, tuple, collections.deque 등 ]
# Flat : 한 개의 자료형만 저장 가능[str, bytes, bytearray, array.array, memeryview]
# 가변: list, bytearray, array.array, memoryview, deque
# 불변: tuple, str, bytes

# 지능형 리스트(Comprehending List, List Comprehension)

# Non Comprehending List
chars = '!@#$%^&*()_+'
codes1 = []
for s in chars:
  codes1.append(ord(s))
print('EX1-1 - ', codes1)

# Comprehending Lists
# 성능에 대해서는 내부 데이터 수가 현저히 많이 늘어날 경우는 list comprehension이 조금 더 좋다고 알려져 있음.
# 일반적으로 코딩할때는 큰 차이는 없음.
codes2=[ord(s) for s in chars]
print(codes2)

# Comprehending Lists
# 개발자들이 보통 말하는 속도 약간 우세한 경우
# 이렇게 조건이 걸려 있는 경우는 list comprehension이 더 빠르다고 함.
codes3 = [ord(s) for s in chars if ord(s) > 40]

# Comprehending Lists + Map, Filter 이렇게도 이용 가능함.
codes4 =list(filter(lambda x : x>40, map(ord, chars)))

print()
print()
print('EX1-5 - ', [chr(s) for s in codes1])

print()
print()

# Generator 값을 하나씩 생성해 내는 것.
# 단일 한개의 자료형만 저장할 거면 flat인 array가 나음.
# Generator는 한 번에 한개의 항목을 생성(메모리에 유지 하지 않음). 성능이 압도적으로 좋음.
import array
tuple_g = (ord(s) for s in chars)
# 이러니깐 Generator가 만들어짐.
print('EX2-1 - ', tuple_g)
# tuple_g 안에는 맨 처음 나온 값을 바라보고 있음.
# 아직 메모리에 생성은 안하고 입장 안하고 기다리고 있는 단계
# 리스트는 메모리에 다 올리는 것. 메모리의 사용량이 높음. 천개 만개 정도는 별로 상관 없음.
# 한 천만개 몇천억개 이러면 차이가 남.

# NEXT를 사용하면, 그때부터 하나씩 커서 옮겨가며 나오기 시작함.
print('EX2-2 ', next(tuple_g))
print('EX2-3 ', next(tuple_g))
print('EX2-3_1 ', next(tuple_g))

# array는 첫번째 자료형을 알려줌. int
array_g = array.array('I', (ord(s) for s in chars))
print('EX2-4 - ', array_g)
print('2-5.', array_g.tolist())


print()
print()

# 제네레이터 예제
# List Comprehension을 튜플로 묶으면 Generator가 나오고, List로 묶으면 리스트가 나열됨.
# Generator는 실행 시점에 값을 반환해서 메모리를 아낌.next 나 for 등이 나오기 전에는 값을 반환하지 않음.
print('3-1. ', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))
print('3-2. ', ['%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)])

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
  print('3-3. ', s)

print()
print()

# List 사용 시 주의할 점. Critical한 실수
marks1 = [['~']*3 for n in range(3)]
marks2 = [['~']*3]*3
print('4-1', marks1)
print('4-2', marks1)
#  같아 보이는데 큰 차이가 있음.
print()
marks1[0][1]='X'
marks2[0][1]='X' #모든 리스트의 두번째 인덱스가 다 바뀜.
print("===============")
# 이거까지 똑같다는거는 곱하기를 쓰면 그대로 id 통으로 복제된다는 거네.
# 사실은 marks2는 그냥 모든 원소가 다 같은 id를 가리키고 있음.
print(id(marks2[0][0]), id(marks2[0][2]))
print("===============")
print('4-4', marks1)
print('4-5', marks2)
# Why?
# Proof
print('4-5. ', [id(i) for i in marks1])
print('4-6. ', [id(i) for i in marks2])
# 밖에서 곱하면, 복제해서 넣는게 되어버림.
a= ['asdf']*3
print([id(b) for b in a])
print()
print()
print()

#Tuple -> Packing(넘길때 싸서 넘기는 것), Unpacking(풀어서 받는 것), Immutable

print('5-1 - ', divmod(100, 9))
# 인자 2개를 넘겨야 되는데 아래는, 묶여서 하나로 왔음. 이럴 때, *를 써서 패킹으로 넘김.
#알아서 풀어서 사용하라는 뜻.
print('5-2 - ', divmod(*(100, 9)))
print('5-3 - ', *(divmod(100, 9)))

print()

x, y, *rest = range(10)
print('5-4 - ', x, y, rest)

x, y, *rest = range(2)
print('5-5 - ', x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print('5-6 - ', x, y, rest)
# 기본적으로 *이 있으면, *한개는 언팩킹으로 사용하겠다는 뜻이고, * 2개는 딕셔너리 형태로 사용하겠다는 것.
# def sample(*args, **args) 이런 것
# https://brunch.co.kr/@princox/180

print()
print()

# Mutable(불변) vs Immutable(불변)
l = (10, 15, 20)
m = [10, 15, 20]

print('6-1 - ', l, m, id(l), id(m))

#아래 표현식의 경우, 리스트와 튜플 모두 새로운 객체에 할당
l = l*2
m = m*2
print('EX6-2', l, m, id(l), id(m))
# print(dir(l))
# print(l.__mul__)

#아래 표현식의 경우는, 리스트는 그대로 튜플 모두 새로운 객체에 할당(immutable하니깐)
l *= 2
m *= 2
print('EX6-3', l, m, id(l), id(m))

# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']

# sorted : 정렬 후 새로운 객체가 반환됨.
# key는 함수를 받음. 어떤 함수는 정의해서 넣으면 됨.
print('EX-7 - 1', sorted(f_list))
print('EX-7 - 2', sorted(f_list, reverse=True))
print('EX-7 - 3', sorted(f_list, key=len)) #문자열 길이로 정렬해줌
print('EX-7 - 4', sorted(f_list, reverse=True, key=lambda x:x[-1])) # 키 에다가 마지막 글자를 주는 거지. 그거 대로 정렬
# 원본은 변경되지 않음.
print('EX-7 - 5', sorted(f_list))

# sort: 정렬 후 객체 직접 변경
# 파이썬에서는 None이 반환되면 이 함수는 반환값이 없는 함수라는 것에 대한 signal
a = f_list.sort()
# a -> None, f_list has been changed!
print(a, f_list)

print('EX7-7 - 6', f_list.sort(), f_list)
print('EX7-7 - 7', f_list.sort(reverse=True), f_list)
print('EX7-7 - 8', f_list.sort(key=len), f_list)
print('EX7-7 - 9', f_list.sort(key=lambda x:x[-1], reverse=True), f_list)





