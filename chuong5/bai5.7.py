import sqlite3

database_name = "bai5_5.db"

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

new_age = 40
cursor.execute("UPDATE users SET age = ?;", (new_age,))

conn.commit()

cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()