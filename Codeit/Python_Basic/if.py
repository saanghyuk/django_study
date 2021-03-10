def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    # 코드를 쓰세요.
    if total >=90:
        print("A")
    elif total < 90 and total >= 80:
        print("B")
    elif total <80 and total >= 70:
        print("C")
    elif total < 70 and total >= 60:
        print("D")
    else:
        print("F")


# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

i=1
while i<=100:
    if i%8 ==0 and i%12 != 0:
        print(i)
    i += 1

house=1100000000
money = 50000000
i = 1988
while i <= 2015:
    i += 1
    money*= 1.12
    print("{}년의 금액은 {}입니다.".format(i, money))
#
# difference=house-money
# if(house>money):
#     print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(round(difference)))
# elif:
#     print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(round(difference)))

# list = [1, 1]
# i = 3
# while i <= 50:
#     next = list[i - 3] + list[i - 2]
#     list.append(next)
#     print(next)
#     i += 1

#

i = 1
j = 1

while i<= 9:
    while j<= 9:
        print("{}*{}={}".format(i, j, i*j))
        j+=1
    print(i)
    i+=1