#section12-3
#파이썬 데이터베이스 연동
#테이블 데이터 수정 및 삭제

import sqlite3

conn = sqlite3.connect('./resource/database.db')
c = conn.cursor()

#fix 1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

#fix 2
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'goodman', 'id': 5})

#fix 3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', '4'))

#middle data check1
for user in c.execute("SELECT * FROM users"):
  print(user)

#Row Delete1
c.execute("DELETE FROM users WHERE id =?", (2,))

#Row Delete2
c.execute("DELETE FROM users WHERE id =:id", {"id":5})

#Row Delete3
c.execute("DELETE FROM users WHERE id =%s" % (4))

#middle data check
for user in c.execute("SELECT * FROM users"):
  print(user)

#Remove Entire Data
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, " rows")


conn.commit()

#
conn.close()
