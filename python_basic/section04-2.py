#Section 04-2
#문자열, 문자열연산, 슬라이싱

str1 = "I am Boy."
str2 = "Niceman"
str3 = ''
str4 = str()

print(len(str1), len(str2), len(str3), len(str4))


#Escape
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tap \t"
print(escape_str2)

#Raw String, \등의 특수문자까지 모두 보여줌.
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\a"
print(raw_s2)

#멀티라인 몇줄로 할때, \를 쳐야 그 다음 줄에 이어진다고 파이썬에게 알려준 것.
#변수선언 한다음에 escape하나 치면  다음줄에 뭔가 이어진다는 signal
multi = \
""""
문자열

멀티라인

테스트
"""
print(multi)

#문자열 연산
str_o1 = "*"
str_o2 = "abc"
str_o3 = "def"
str_o4 = "Niceman"
print(str_o1*100)
print(str_o1+str_o2)
print('a' in str_o4) #a가 있는지를 묻는 것
print('f' in str_o4)
print('z' not in str_o4)



#List, Tuple
