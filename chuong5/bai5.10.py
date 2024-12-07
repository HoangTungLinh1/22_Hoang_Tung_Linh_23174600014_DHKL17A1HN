import sqlite3

conn = sqlite3.connect("product.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
)
''')
conn.commit()
conn.close()

def hien_thi_sp():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    conn.close()
    for product in products:
        print(product)

hien_thi_sp()

def them_sp(id, name, price, amount):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO product (Id, Name, Price, Amount) VALUES (?, ?, ?, ?)", (id, name, price, amount))
    conn.commit()
    conn.close()

them_sp(1, "PC", 1000.0, 100)

def cap_nhat_sp(id, new_price, new_amount):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE product SET Price = ?, Amount = ? WHERE Id = ?", (new_price, new_amount, id))
    conn.commit()
    conn.close()

cap_nhat_sp(1, 1600.0, 150)

def xoa_sp(id):
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE Id = ?", (id,))
    conn.commit()
    conn.close()

xoa_sp(1)

