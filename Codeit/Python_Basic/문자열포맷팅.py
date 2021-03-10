
#문자열 포맷팅
year=2019
month=10
day=29
print("오늘은"+str(year)+"년"+str(month)+"월"+str(day)+"일")


print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))
date_string="오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
print(date_string.format(year, month, day+1))

#순서 바꾸기
print("저는 {1}, {0}, {2}를 좋아합니다.".format("박지성", "유재석", "빌게이츠"))

num_1=1
num_2=3
print("{0} 나누기 {1}은 {2:.2f} 입니다.".format(num_1, num_2, num_1/num_2))
#.2f는 .2는 소숫점 둘째짜리로 반올림 하라는 뜻. f는 floating point의 약자임.