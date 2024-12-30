import tkinter as tk

window = tk.Tk()

window.title("tk")
window.geometry("400x300")

tk.Label(window, text="Student Name:").place(x=50, y=50)
ten_SV = tk.Entry(window)
ten_SV.place(x=150, y=50, width=200)

tk.Label(window, text="Student ID:").place(x=50, y=100)
id_SV = tk.Entry(window)
id_SV.place(x=150, y=100, width=200)

tk.Label(window, text="Password:").place(x=50, y=150)
mat_khau = tk.Entry(window, show="*")
mat_khau.place(x=150, y=150, width=200)

tk.Button(window, text="Gửi", command=lambda: print(f"Tên: {ten_SV.get()}, ID: {id_SV.get()}, Mật Khẩu: {mat_khau.get()}"))\
    .place(x=150, y=200, width=100)

window.mainloop()