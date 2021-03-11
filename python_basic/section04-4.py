#section04-4
#파잇너 데이터 타입(자료형)
#딕셔너리, 집합 자료형

#딕셔너리(Dictionary): 순서X, 중복X(Key가 중복이 안된다는 것, 값은 중복 가능), 수정O, 삭제O

#Key, Value(Json) -> MongoDB

a = {'Name': 'SON', 'Phone':'010-0000-0000', 'birth': 870214}
b = {0: 'Hello, Python', 1: 'Hello, Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(type(a))

#출력
print(a['Name'])
print(a.get('Name'))
print(a.get('address')) #Get Method는 안전하게 빼게 해줌. error를 안터드리고 None이라고만 나옴.
print(c['arr'][1:2])


#딕셔너리 추가
a['address']= 'Incheon'
print(a)
a['rank']=[1, 3, 4]
print(a)
a['rank2'] = (1, 3, 4)
print(a)

#keys, values, items
print(a.keys()) #생긴거는 리스트 처럼 생겼는데, 인덱스로 접근이 안됨. print(a.keys()[0]) 불가
temp=list(a.keys())
print(temp[0])
print(a.values())

print('items')
print(a.items())
print(list(a.items()))
print(1 in b) # Key를 찾는 것.
print('name' in b)

#집합 -> 순서 X, 집합 X
a=set()
b=set([1, 2, 3, 4])
c=set([1, 4, 5, 6, 6])
print(c) #나는 1, 4, 5, 6, 6 을 넣었는데, 1, 4, 5, 6만 나옴. 집합이기 때문.
t=tuple(b)
print(t)
l = list(b)
print(l)

s1=set([1, 2, 3, 4, 5, 6])
s2=set([4, 5, 6, 7, 8, 9])

#교집합
print(s1.intersection(s2))
print(s1 & s2)
#합집합
print(s1.union(s2))
print(s1 | s2)
#차집합
print(s1-s2)
print(s1.difference(s2))

#추가, 제거
s3=set([7, 8, 10, 15])
s3.add(10)
s3.add(7) #중복 허용X

s3.remove(15)
print(s3)

print(type(s3))