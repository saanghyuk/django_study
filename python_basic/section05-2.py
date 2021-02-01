#Section05-2
#파이썬 흐름제어 반복문

#코딩의 핵심 -> 조건 해결 중요
#기본 반복문은 for과 while

v1 = 1
while v1 < 11:
  print("v1 is", v1)
  v1+=1

for v2 in range(10):
  print("v2 is :", v2)

for v3 in range(1, 11):
  print("v3 is :", v3)

#1~10합
sum1 = 0
cnt1 = 0
while cnt1<=100:
  sum1 += cnt1
  cnt1 += 1

print('1~100 : ', sum1)
print('1~100 : ', sum(range(1, 101)))
print('1~100 : ', sum(range(1, 100, 2)))


# Sequnce(순서가 있는) 자료형의 반복
# 문자열, 리스트, 튜풀, 집합, 딕셔너리 등을 반복 가능
# iterable: range, reversed,enumerate, filer, map, zip

names = ["Kim", 'Park', "Jo", 'Choi', "Son"]
for name in names:
  print(name)

word = "sanghyukSon"

for s in word:
  print("Word : ", s)

my_info = {
  "name":"Son",
  "age": 29,
  "city": "Incheon"
   }

#이러면, 키만 반복
for key in my_info:
    print("My info", key)
#value 반복
for key in my_info.values():
    print("My info", key)
#items
for key, value in my_info.items():
    print("My key", key, "My value", value)

name = "KennRy"

for n in name:
  if n.isupper():
    print(n)
  else:
    print(n.upper())

#Break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for n in numbers:
  if n == 33:
    print('Find 33')
    break
  else:
    print("Not Found")

#for else 구문 반복문이 정상적으로 실행되면, else블록 시행
for n in numbers:
  if n == 100:
    print('Find 33')
    break
  else:
    print("Not Found")
else: #break문을 끝까지 안만나면, 다 시행된 다음에, else문이 시행됨.
  print("Not found 33.....")

#Continue, 이걸 만나면 다음 수행할 곳으로 간다는 것.
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
  if type(v) is float:
    continue
  print(type(v))




