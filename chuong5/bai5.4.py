import sqlite3

conn = sqlite3.connect("bai5_2.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Các bảng trong cơ sở dữ liệu:")
for table in tables:
    print(table[0])

conn.close()
