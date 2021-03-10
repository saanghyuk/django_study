# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
# 모두 다 가능
print('Helllo, Python!')
print("Hello, Python!")
print('''Hello, Python''')
print("""Hello, Python""")

print()  # 그냥 이렇게만 쓰면 줄바꿈

# Seperator 옵션 사용
print('T', 'E', 'S', 'T', sep='')  # Seperator 없애라는 거지
print('2019', '02', '19', sep='-')
print('niceman', 'google.com', sep='@')
print()
# end 옵션 사용
# end=''을 쓰면 줄바꿈이 사라지네
print('Welcome To', end=', ')
print('the black parade', end=' ')
print('piano notes')
print()

# format 사용
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))


# %s: 문자, %d: 정수, %f: 실수
print("%s's favorite number is %f, %d" % ('Sanghyuk', 7, 8))


# 5d? 정수부분 다섯자리, 4.2f는 정수부분 4자리 소수부분 2자리
print('Test1: %2d, Price: %4.10f' % (776, 6534.123))
# 아래처럼도 가능
print("Test1 : {0: 5d}, Price: {1:4.2f}".format(776, 6534.123))
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))

# Escape

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print('\'you\'')
print("'you'")
print('"you"')
print("""'you'""")
print("hihi")
print("hi\000hi")
print('\t\t\t\tHello, World')
