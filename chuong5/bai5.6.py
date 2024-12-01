import sqlite3

database_name = "bai5_5.db"

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM users;")
count = cursor.fetchone()[0]

print(f"Số bản ghi trong bảng 'users': {count}")

conn.close()
