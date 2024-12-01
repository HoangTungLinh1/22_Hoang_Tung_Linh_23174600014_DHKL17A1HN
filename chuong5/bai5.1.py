import sqlite3

conn = sqlite3.connect("bai5_1.db")

print("Phiên bản SQLite:", sqlite3.sqlite_version)

conn.close()
