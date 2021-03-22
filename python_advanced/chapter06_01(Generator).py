# 지금까지는 하나의 흐름을 가지고 위에서 아래로 실행시킴
# 동시성은 A, B, C를 한번에 처리시키는 거야.

# Chapter06-01
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# Generator, 반복형

# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, Unpacking, *args
# 반복형 객체 내부적으로 iter함수 내용, 제네레이터 동작 원리, yield from

# 반복 가능한 이유? -> iter(x)함수를 내부적으로 호출하기 때문에 우리가 사용할 수 있는 것.
# https://docs.python.org/ko/3/library/collections.abc.html#collections.abc.Iterable



t = 'ABCDEF'
# for
for c in t:
  print('EX1-1 - ', c)


print()

# While 사용
w = iter(t)
while True:
  try:
    print('EX1-1 - ', next(w))
  except StopIteration as log:
    print(log)
    break

# collections
from collections import abc
# 반복형(Iter) 확인 가능
print('EX1-3 -', hasattr(t, '__iter__'))
print('EX1-4 -', isinstance(t, abc.Iterable))
print('EX1-4 _1 - ', dir(t)) # __iter__가 나오면 반복 가능하다는 것.

print()
print()

# next 사용
# list는 iterator로 변환이 가능하므로, iterable한 객체이다.
# 일단 iterable해야 iterator로 변환이 가능한 듯.
# iterator는 next를 쓸 수 있는 객체의 type

class WordSplitIter:
  def __init__(self, text):
    self._idx = 0
    self._text = text.split(' ')

  def __next__(self): # Iterator(next) 처럼 만들기
    print('Called __next__')
    try:
      word = self._text[self._idx]
    except IndexError:
      raise StopIteration('Stop!! Stop!!')

    self._idx += 1
    return word

  def __iter__(self): # Iterable(for) 만들기
    print('Called __iter__')
    return self

  def __repr__(self):
    return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Who says the nights are for sleeping')
# print(wi._text)
# print(type(wi)) 타입은 iterator가 아닌데 class내부에서 오버라이딩 해서, iterable(for)하게 만들고, iterator(next)처럼 쓸 수 있게 만든 것.
print('EX2-1- ', wi) # repr로 출력이 되는 것.
print('EX2-2- ', next(wi))
print('EX2-3- ', next(wi))
print('EX2-4- ', next(wi))
print('EX2-5- ', next(wi))
print('EX2-6- ', next(wi))
print(type(wi))
for i in wi:
  print(i) # __iter__함수 빼면 에러 TypeError: 'WordSplitIter' object is not iterable 나옴. 당연하지 iter은 안넣었으니깐

# 끝까지 가보면 Stop Iteration

# 발전기에서 생산하듯이 하나씩 필요할때마다 반환해 주는 게 Generator

print()
print()


# self 학습!
# iter 객체로 바꾸면 원래도 for 다 돌고 나서, next()하면 StopIteration에러 뜨는게 당연한 것.
i = [1, 2, 3, 4, 5]
i = iter(i)
for j in i:
  print(j)
# print(next(i))


# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가될 경우 메모리 사용량 증가 -> 제네레이터를 사용해서 완화함
# 2. 단위 실행 가능한 코루틴(Coroutine)구현에 아주 중요함.
# 3. 배열이나, 딕셔너리, 리스트 등은 한번 호출할 때 마다 하나의 값만 리턴해 줌. -> 아주 작은 메모리 양을 필요로 함.
# 즉, 리스트 안에 천만개 있어? 그거 하나의 리스트에 담는게 너무 메모리가 많이 들어가. 제네레이터는 만들면서 하나씩만 가져오고, 다음에 가져올 위치만 기억하잖아.


class WordSplitGenerator:
  def __init__(self, text):
    self._text = text.split(' ')

  def __iter__(self):
    for word in self._text:
      yield word #  Generator, 이게 next에서 코드 썻던거 다 해주는 거야.
    return

  def __repr__(self):
    return 'WordGenerator(%s)' % (self._text)



wg = WordSplitGenerator('Who says the nights are for sleeping')
print(type(wg))
print(dir(wg))

# print(next(wg))
wt= iter(wg) # iter가 없으면, 애초에
print(dir(wt))
print(type(wt)) # Generator로 바뀜
# print(type(wi))
print('EX3-1- ', wt)
print('EX3-2- ', next(wt))
print('EX3-3- ', next(wt))
print('EX3-4- ', next(wt))
print('EX3-5- ', next(wt))
print('EX3-6- ', next(wt))
print('EX3-7- ', next(wt))
print('EX3-8- ', next(wt))
# print('EX3-9- ', next(wt))

print()
print()

# Generator 예제 1
# 보통은 함수로 활용함
def generator_ex1():
  print('start')
  yield 'AAA'
  print('continue')
  yield 'BBB'
  print('end')

temp = iter(generator_ex1())
# print('EX4-1 - ', next(temp))
# print('EX4-1 - ', next(temp))
# print('EX4-1 - ', next(temp))

# Generator는 for에서 진가를 발휘함. for는 예외를 알아서 잡아주기 떄문
# Stop Iterator앞에서 딱 멈춰주는 것.
for v in generator_ex1():
  pass
  # print('EX4-3 - ', v)


# Generetor 예제 2 빅데이터 다루려면, 정말 generator를 잘 알아야 함.
temp2 = [x * 3 for x in generator_ex1()] #['AAAAAAAAA', 'BBBBBBBBB']
temp3 = (x * 3 for x in generator_ex1()) #<generator object <genexpr> at 0x7f9a0cf4ae60>

print('EX5-1 - ', temp2)
print('EX5-2 - ', temp3) # 얘는 generator형태로 가지고 있음.

for i in temp2:
  print('EX5-3 - ', i)

print()
print()

for i in temp3:
  print('EX5-4 - ', i)

print()
print()

# Generator 예제 3 (자주 사용하는 함수)
# count, takewhile,filterfalse, accuulate,chain, product, groupby
import itertools

gen1 = itertools.count(1, 2.5) # 1부터 2.5씩 증가하면서 무한대로 만들고 싶은 경우
#무한
print('EX6-1 - ', next(gen1))
print('EX6-2 - ', next(gen1))
print('EX6-3 - ', next(gen1))
print('EX6-4 - ', next(gen1))
print('EX6-5 - ', next(gen1))


# 조건
gen2 = itertools.takewhile(lambda n : n<1000, itertools.count(1, 2.5))

for v in gen2:
  print('EX6-5 - ', v)

print()
print()

# 필터 반대
# 해당 조건을 제외한 나머지들이 나오게 됨.
gen3 = itertools.filterfalse(lambda n : n<3, [1, 2, 3, 4, 5])
for i in gen3:
  print('EX6-6 - ', i)

print()
print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])
for v in gen4:
  print('EX 6-7 - ', v)

print()
print()

# 연결 1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))
print('EX6-8', list(gen5))

# 연결 2
gen6 = itertools.chain(enumerate('ABCDE'))
for i, v  in enumerate('ABCDE'):
  print(i, v)
print('EX6-9', list(gen6))

print()
print()

# 개별
gen7 = itertools.product('ABCDE')
print('EX6-10', list(gen7)) #[('A',), ('B',), ('C',), ('D',), ('E',)]
# for i in gen7:
#   print(i)

print()
print()


# 연산(경우의 수) 2면 2개 1쌍, 3이면 3개가 1쌍
gen8 = itertools.product('ABCDE', repeat = 2 )
print('EX6-12', list(gen8))

print()
print()


# 그룹화
gen9 = itertools.groupby('AAAABBBCCCCDDEEEE')
#print('EX6-12', list(gen9))
for chr, group in gen9:
  print('EX6 - 12 - ', chr, ':', list(group))
