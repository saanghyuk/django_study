#section05-1
#파이썬 프름제어(제어문)
#조건문 실습

print(type(True))
print(type(False))

#예1
if True:
  print("Yes")

if False:
  print("No")
else:
  print("Yes2")

#관계 연산자
# >, >=, <, <=, !=
a = 10
b = 0
print(a==b)
print(a!=b)

#참 거짓 종류(True, False)
#참: "내용", [내용], (내용), {내용}, 1
#거짓 : "", [], (), {}, 0

#논리연산자
#and or not
a=100
b=60
c=15

print('and : ', a>b and b>c)
print('or : ', a>b or c>b)
print('not : ', not a>b)

#산술, 관계, 논리연산자
#산술 > 관계 > 논리 순서로 적용
print('ex1:', 5 + 10 > 0 and not 7 + 3 ==10) #5+10 먼저, 그 다음에 >나 ==, 그 다음 and not

score1=90
score2='A'

if score1 >= 90 and score2 =='A':
  print("합격")
else:
  print("불합격")

#다중조건문
num=90
if num>90:
  print("A")
elif num>=80:
  print("B")
elif num>=70:
  print("C")
else:
  print("D")

#중첩 조건문
age=27
height=175

if age >=20:
  if height >=170:
    print('합격')
  elif height >=160:
    print('예비')
  else:
    print('불합격')
else:
  print('20세 이상 지원가능')


