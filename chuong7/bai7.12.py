import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x450")

tk.Label(window, text="Cân nặng (kg):").pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Chiều cao (m):").pack()
height_entry = tk.Entry(window)
height_entry.pack()

bmi_label = tk.Label(window, text="")
bmi_label.pack()

category_label = tk.Label(window, text="")
category_label.pack()

def tính_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        bmi = weight / (height ** 2)
        
        category = "Bình thường"
        if bmi < 18.5:
            category = "Nhẹ cân"
        elif bmi > 24.9:
            category = "Thừa cân"
        
        bmi_label.config(text=f"BMI: {bmi:.2f}")
        category_label.config(text=f"Kết luận: {category}")
    
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập cân nặng và chiều cao hợp lệ.")

tk.Button(window, text="Tính BMI", command=tính_bmi).pack()

window.mainloop()

