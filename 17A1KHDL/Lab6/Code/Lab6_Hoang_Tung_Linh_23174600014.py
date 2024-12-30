import sqlite3
from tkinter import *

def connect_db():
    conn = sqlite3.connect("product.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        tên sản phẩm TEXT NOT NULL,
        giá sản phẩm REAL,
        số lượng INTEGER NOT NULL
    )
    """)
    conn.commit()
    return conn

def them_sp():
    ten_sp = ten_sp_vao.get()
    gia_sp = gia_sp_vao.get()
    so_luong = so_luong_vao.get()

    if ten_sp and gia_sp and so_luong:
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO product (ten_sp, gia_sp, so_luong) VALUES (?, ?, ?)", (ten_sp, float(gia_sp), int(so_luong)))
            conn.commit()
            conn.close()
            update_listbox()
            xoa_cac_truong()
            messagebox.showinfo("Thành công", "Thêm sản phẩm thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể thêm sản phẩm: {e}")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")

def cap_nhat_listbox():
    listbox.delete(0, END)
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    conn.close()
    for product in products:
        listbox.insert(END, f"ID: {product[0]}, ten_sp: {product[1]}, gia_sp: {product[2]}, so_luong: {product[3]}")

def xoa_sp():
    selected_item = listbox.curselection()
    if selected_item:
        item_text = listbox.get(selected_item)
        product_id = item_text.split(",")[0].split(":")[1].strip()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM product WHERE Id = ?", (product_id,))
        conn.commit()
        conn.close()
        update_listbox()
        messagebox.showinfo("Thành công", "Xóa sản phẩm thành công!")
    else:
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một sản phẩm để xóa!")

def xoa_cac_truong():
    ten_sp_vao.delete(0, END)
    gia_sp_vao.delete(0, END)
    so_luong_vao.delete(0, END)

Window = Tk()
Window.title("Quản Lý Sản Phẩm")
Window.geometry("600x400")

Label(Window, text="Tên sản phẩm:").grid(row=0, column=0, padx=10, pady=5)
ten_sp_vao = Entry(Window, width=30)
ten_sp_vao.grid(row=0, column=1, padx=10, pady=5)

Label(Window, text="Giá sản phẩm:").grid(row=1, column=0, padx=10, pady=5)
gia_sp_vao = Entry(Window, width=30)
gia_sp_vao.grid(row=1, column=1, padx=10, pady=5)

Label(Window, text="Số lượng:").grid(row=2, column=0, padx=10, pady=5)
so_luong_vao = Entry(Window, width=30)
so_luong_vao.grid(row=2, column=1, padx=10, pady=5)

Button(Window, text="Thêm sản phẩm", command=them_sp).grid(row=3, column=0, padx=10, pady=10)
Button(Window, text="Xóa sản phẩm", command=xoa_sp).grid(row=3, column=1, padx=10, pady=10)

listbox = Listbox(Window, width=80, height=15)
listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

cap_nhat_listbox()

Window.mainloop()
