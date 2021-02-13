#Section 13-1
#업그레이드 타이핑 게임 제작
#타이핑 게임 제작 및 기본 완성
 # -*- coding: euc-kr -*-
import random
import time
import pygame
import sqlite3
import datetime

#DB & Auc\to Commit
#DB path
conn = sqlite3.connect('./resource/records.db', isolation_level=None)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text)")


words =[] #영어 단어 리스트(1000개 로드)
n=1
cor_cnt =0 #정답 갯수

with open('./resource/word.txt', 'r') as f:
  for c in f:
    words.append(c.strip())

# print(words) #check wordlist

input('Ready? Press Enter Key!') #Enter Game Start
start = time.time()
pygame.init()
pygame.mixer.init()

while n <= 5 :
  random.shuffle(words)
  q = random.choice(words)
  print()
  print(q) #문제 출력

  x = input() #타이핑 입력

  if str(q).strip() == str(x).strip():
    print("Pass!")
    corr_sound= pygame.mixer.Sound("./sound/good.wav")
    corr_sound.play()
    cor_cnt+=1

  else:
    print("Wrong!")
    wrong_sound= pygame.mixer.Sound("./sound/bad.wav")
    wrong_sound.play()

  n+=1


end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
  print("합격")
else:
  print("불합격")

#DB INSERTION
cursor.execute("INSERT INTO records(cor_cnt, record, regdate) VALUES (?,?,?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


print("게임 시간 : ", et, "초", "정답 개수 : {}".format(cor_cnt))

#시작 지점인 경우에만 실행해라
if __name__ == '__main__':
  pass
