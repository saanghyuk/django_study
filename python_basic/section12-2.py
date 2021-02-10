#Section12-2
#파이썬 데이터베이스 연동
#테이블 조회

import sqlite3

conn = sqlite3.connect('./resource/database.db') #my db route

#cursor binding
c = conn.cursor()

#read
c.execute("SELECT * FROM users")

#cursor 위치 변경
#1개 로우 선택
# print('One -> \n', c.fetchone())

# print('Three -> \n', c.fetchmany(size = 3 ))

# #전체 로우 선택
# print('All -> \n', c.fetchall()) #next all

# print()


#순회
#case 1
# rows = c.fetchall()
# for row in rows:
#   print('retrieve1 -> ', row)

#case 2
# for row in c.fetchall():
#   print('retrieve2 -> ', row)

#case 3
# for row in c.execute('SELECT * FROM users ORDER BY id desc'):
#     print('retrieve3 -> ', row)




#WHERE Retrieve1
# param1 = (3,)
# c.execute('SELECT * FROM users WHERE id=?', param1)
# print('param1', c.fetchone())
# print('param1', c.fetchall()) #하나만 뽑아온 상태라서 이후 커서에서 다 가져올 애가 없음.


#WHERE Retrieve 2
# param2 = 4
# c.execute('SELECT * FROM users WHERE id="%s"' % param2)
# print('param2', c.fetchone())
# print('param2', c.fetchall()) #하나만 뽑아온 상태라서 이후 커서에서 다 가져올 애가 없음.


#WHERE Retrieve 3
# c.execute('SELECT * FROM users WHERE id=:Id', {"Id": 5})
# print('param3', c.fetchone())
# print('param3', c.fetchall()) #하나만 뽑아온 상태라서 이후 커서에서 다 가져올 애가 없음.

#WHERE Retrieve 4
# param4 = (3, 5)
# c.execute('SELECT * FROM users WHERE id IN(?,?)', param4)
# print('param4', c.fetchall())



#WHERE Retrieve 5
# c.execute("SELECT * FROM users WHERE id IN('%d','%d')", % (3, 4))
# print('param4', c.fetchall())

#WHERE Retrieve 6
c.execute("SELECT * FROM users WHERE id= :id1 OR id= :id2", {"id1" : 2, "id2": 5})
print('param6', c.fetchall())

#Dump 출력. 데이터베이스 백업
with conn:
  with open('./resource/dump.sql', 'w') as f:
    for line in conn.iterdump():
      f.write('%s\n' %line)

    print('Dump Print Complete')

#f.close(), conn.close()




