import sqlite3

database_name = "bai5_5.db"

conn = sqlite3.connect(database_name)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS users;")

conn.commit()

conn.close()
