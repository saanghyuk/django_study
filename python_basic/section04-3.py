#Section04-3
#List, Tuple

#리스트 순서O, 중복O, 수정O, 삭제O
a=[]
b=list()
c=[1, 2, 3, 4]
d=[10, 100, 'Pen', 'Banana', 'Orange']
e=[10, 100, ' Pen', 'Banana', 'Orange', ['Apple', 'Banana']]

#인덱싱
print(d[3])
print(d[-1]+d[-2])
print(e[-1][-1])

#슬라이싱
print(d[0:3])
print(d[0:1])
print(e[-1][0:2])


#연산
print(c+d) #하나의 리스트로 만들어줌
print(c*3)
print(str(c[0])+'hi')

#리스트 수정
c[0]=77
print(c)
#C에서 [1:2]하면 [1]이 남잖아. 그 구간을 아래 3개로 대체하는 거지.
c[1:2]=[100, 1000, 10000]
print(c)
#아래처럼 하나를 쓰고 리스트를 넣으면 nested가 됨.
c[1] = ['a', 'b', 'c']
print(c)

del(c[1])
print(c)

print()
print()

#리스트 함수
y=[5, 2, 3, 1, 4]
print(y)
y.append(6)
print(y)

print("sort")
y.sort()
print(y)
y.reverse()
print(y)
#끝이 아니라 특정인덱스에 넣을 때
y.insert(2, 7) #2번 인덱스에 7을 넣겠다.
y.remove(2) #숫자 2를 찾아서 지우는 것 del은 인덱스 찾는 것.

#맨 마지막꺼 꺼내서 없애버리는 것.
y.pop()
print(y) #LIFO


ex=[88,77]
y.extend(ex)
print(y) #extend는 원소가 들어가줌.

y.append(ex) #append는 리스트 자체로 들어감
print(y)

#삭제: del, remove, pop


#튜플(순서O, 중복O, 수정X, 삭제x)-> 중요한 키값 등을 자주 넣음

a = ()
b = (1,)#마지막은 컴마로 끝내기
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
# error del c[2]
print(c[2])
print(c[3])
print(d[2][2])

print(d[2:])
print(d[2][0:2])

print(c+d)
print(c*3)
print("")

#튜플 함수

z=(5, 2, 1, 3, 4, 3)
print(z)
print(3 in z)
print(z.index(3)) #3의 인덱스를 반환하라
print(z.count(3))

print("------")

print(y.index(3))
print(y.count(3))

