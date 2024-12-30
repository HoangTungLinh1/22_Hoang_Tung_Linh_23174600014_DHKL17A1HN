import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("tk")
root.geometry("400x450")

def menu(hanh_dong):
    if hanh_dong == "1.1":
        messagebox.showinfo("Lập trình hướng đối tượng", "Viết chương trình giải phương trình bậc hai")
    elif hanh_dong == "1.2":
        messagebox.showinfo("Lập trình hướng đối tượng", "Viết chương trình quản lý sinh viên")
    elif hanh_dong == "1.3":
        messagebox.showinfo("Lập trình hướng đối tượng", "Viết chương trình quản lý thư viện")
    elif hanh_dong == "Exit":
        root.quit()

menu_bar = tk.Menu(root)

menu_chapter1 = tk.Menu(menu_bar, tearoff=0)
menu_chapter1.add_command(label="1.1 - Giải phương trình bậc hai", command=lambda: menu("1.1"))
menu_chapter1.add_command(label="1.2 - Quản lý sinh viên", command=lambda: menu("1.2"))
menu_chapter1.add_command(label="1.3 - Quản lý thư viện", command=lambda: menu("1.3"))
menu_chapter1.add_separator()
menu_chapter1.add_command(label="Exit", command=lambda: menu("Exit"))

menu_bar.add_cascade(label="Chương 1", menu=menu_chapter1)

menu_chapter2 = tk.Menu(menu_bar, tearoff=0)
menu_chapter2.add_command(label="2.1 - Bài tập nâng cao 1", command=lambda: messagebox.showinfo("Chương 2", "Bài tập nâng cao 1"))
menu_chapter2.add_command(label="2.2 - Bài tập nâng cao 2", command=lambda: messagebox.showinfo("Chương 2", "Bài tập nâng cao 2"))
menu_bar.add_cascade(label="Chương 2", menu=menu_chapter2)

menu_chapter3 = tk.Menu(menu_bar, tearoff=0)
menu_chapter3.add_command(label="3.1 - Lý thuyết nâng cao", command=lambda: messagebox.showinfo("Chương 3", "Lý thuyết nâng cao"))
menu_bar.add_cascade(label="Chương 3", menu=menu_chapter3)

root.config(menu=menu_bar)

root.mainloop()
