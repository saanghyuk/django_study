#Sectioon12-1
#파이썬 데이터베이스 연동
#테이블 생성 및 삽입

import sqlite3
import datetime

now = datetime.datetime.now()
print('now : ', now)
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDatetime : ', nowDatetime)

#sqlliste3 version
print('sqlite3.version : ', sqlite3.version )
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version )


#DB생성 & Auto Commit(Rollback)
conn = sqlite3.connect('./resource/database.db', isolation_level=None) #auto commit

#Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

#Table Creation(Data Type: TEXT, NUMERIC, INTEGER, REAL, BLOB)
# c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, \
# regdate text)")


#Data Insertion
c.execute("INSERT INTO users VALUES(1, 'SON', 'sh@naver.com', '010-3030-2030', 'kormat.co.kr', ? )", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)", (2, 'Yoon', 'syoon@gmail.com', '010-6391-4103', 'Yoon.com', nowDatetime ))

#Many 삽입
#튜플과 리스트 형태 삽입 가능
# userList = {
#   (3, 'Lee', 'Lee@naver.com', '010-3213-5325', 'Lee.com', nowDatetime),
#   (4, 'Lin', 'Lin@naver.com', '010-3213-5325', 'Lin.com', nowDatetime),
#   (5, 'Yoo', 'Yoo@naver.com', '010-3213-5325', 'Yoo.com', nowDatetime),
# }

# c.executemany('INSERT INTO users(id, username, email, phone, website, regdate) \
#   VALUES (?,?,?,?,?,?)', userList
#   )


#remove
# conn.execute("DELETE FROM users")

# print("usres db deleted : ", conn.execute("DELETE FROM users").rowcount)

#commit: isolation_level = None 일 경우 자동 반영
#이 옵션 안넣었다면,
#conn.commit() 이걸 해야 반영됨
#커밋 안하고 conn.rollback()했으면 반영이 안되지.


#항상 다 쓰고 접속해제 해놓기
conn.close()


