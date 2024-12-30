import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("tk")
window.geometry("400x250")

tk.Label(window, text="Enter your name:").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Enter your age:").pack()
age_entry = tk.Entry(window)
age_entry.pack()

def ktea_ten():
    name = name_entry.get()
    age = int(age_entry.get())
    if age >= 18:
        messagebox.showinfo("Result", f"Xin chào {name}, Bạn đã trưởng thành!")
    else:
        messagebox.showinfo("Result", f"Xin chào {name}, Bạn còn nhỏ tuổi!")

tk.Button(window, text="Check", command=ktea_ten).pack()

window.mainloop()
