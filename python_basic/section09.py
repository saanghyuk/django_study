#section09
#읽기 모드 : r
#쓰기 모드(기존 파일 삭제) : w
#추가 모드(파일 생성 또는 추가): a
#https://docs.python.org/3.7/library/functions.html#open

#File Reading
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print("-------------dir----------------")
print(dir(f)) # what is f doing?
#close 필수. 안닫으면 반드시 언젠가 예외 발생
f.close()

#example 2, with문은 이 내부에서 작업 끝나면 자동으로 끝내줌.
with open('./resource/review.txt', 'r') as f:
  c = f.read()
  print(c)
  print(list(c))
  print(iter(c))


print("--------------------------")
print("--------------------------")


#example 3
print("EXAMPLE 3")
with open('./resource/review.txt', 'r') as f:
  for c in f: # already iterable 줄마다 iter을 도네.
    print(c)
    print(c.strip())
print("--------------------------")
print("--------------------------")


#example 4
with open('./resource/review.txt', 'r') as f:
  content = f.read()
  print(">", content)
  content = f.read() #한번 읽은 다음에 커서 끝으로 가면 더 읽을 게 없는 것.
  print(">", content)


print("--------------------------")
print("--------------------------")


#example 5
print("#example 5")
with open('./resource/review.txt', 'r') as f:
  line = f.readline()
  print(line)
  while line:
    print(line, end='=====')
    line = f.readline()

print("--------------------------")
print("--------------------------")


#example 6
with open('./resource/review.txt', 'r') as f:
  contents = f.readlines()
  print(contents)


print("--------------------------")
print("--------------------------")


#example 7
with open('./resource/review.txt', 'r') as f:
  contents = f.readlines()
  for c in contents:
    print(c, end = '******')


print("--------------------------")
print("--------------------------")


#example 8

score = []
with open('./resource/score.txt', 'r') as f:
  for line in f:
    print(line)
    score.append(int(line))
  print(score)
print('Average : {:6.3}'.format(sum(score)/len(score)))


#Writing
print("--------------------------")
print("--------------------------")

#example1
with open('./resource/text1.txt', 'w') as f:
  f.write('Niceman\n')

#example2
with open('./resource/text1.txt', 'a') as f:
  f.write('Niceman!\n')

#example3
from random import randint

with open('./resource/text2.txt', 'w') as f:
  for cnt in range(6):
    f.write(str(randint(1, 50)))
    f.write('\n')

#example 4
#write lines : list to file
with open('./resource/text3.txt', 'w') as f:
  list = ['Kim\n', 'Park\n', 'Son\n']
  f.writelines(list)

# with open('./resource/text3_1.txt', 'w') as f:
#   list = ['Kim\n', 'Park\n', 'Son\n']
#   f.write(list) 리스트는 쓸 수가 없음.



#example 5
#파일로 로그 기록할때 가끔 보이는 패턴
with open('./resource/text4.txt', 'w') as f:
  print('Test Contents1!', file=f)
  print('Test Contents2!', file=f)




