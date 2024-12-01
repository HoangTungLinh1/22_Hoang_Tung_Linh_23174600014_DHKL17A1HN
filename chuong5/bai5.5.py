import sqlite3

database_name = "bai5_5.db"

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    );
""")

cursor.execute("INSERT INTO users (name, email, age) VALUES ('Hung', 'hung@gmail.com', 25);")
cursor.execute("INSERT INTO users (name, email, age) VALUES ('Dung', 'dung@gmail.com', 30);")
cursor.execute("INSERT INTO users (name, email, age) VALUES ('Nguyen', 'nguyene@gmail.com', 35);")

conn.commit()

cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

print("Các bản ghi trong bảng 'users':")
for row in rows:
    print(row)

conn.close()
