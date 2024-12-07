import sqlite3

conn = sqlite3.connect("ql_nhan_vien.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS PHONG (
    id INTEGER PRIMARY KEY,
    ho_ten TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS NHAN_VIEN (
    id INTEGER PRIMARY KEY,
    tuoi INTEGER NOT NULL,
    dia_chi TEXT NOT NULL,
    luong REAL NOT NULL,
    Id_phong INTEGER,
    FOREIGN KEY(Id_phong) REFERENCES PHONG(id)
)
''')
conn.commit()
conn.close()

def them_phong_ban(id, name):
    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO PHONG (id, ho_ten) VALUES (?, ?)", (id, name))
    conn.commit()
    conn.close()

them_phong_ban(1, "nhân sự")

def them_nv(id, tuoi, dia_chi, luong, id_phong):
    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO NHAN_VIEN (id, tuoi, dia_chi, luong, Id_phong) VALUES (?, ?, ?, ?, ?)", (id, tuoi, dia_chi, luong, id_phong))
    conn.commit()
    conn.close()

them_nv(1, 30, "Hà Nội", 1000.0, 1)

def hien_thi_nv():
    conn = sqlite3.connect("ql_nhan_vien.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM NHAN_VIEN")
    employees = cursor.fetchall()
    conn.close()
    for emp in employees:
        print(emp)

hien_thi_nv()

