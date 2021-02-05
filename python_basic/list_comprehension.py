#List Comoprehension
#리스트 컴프리핸션


numbers = []
for n in range(1, 100):
  numbers.append(n)

print(numbers)


numbers2 = [x for x in range(1, 100)]
print(numbers2)


#example
q3 = ["갑", "을", "병", "정"]
q5 = [x for x in q3 if x != "정"]

print(q5)
q6 = [x for x in range(1, 101) if x%2 !=0]
print(q6)


