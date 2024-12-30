import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("400x450")

tk.Label(window, text="Nhập khoảng cách (km):").pack()
khoang_cach = tk.Entry(window)
khoang_cach.pack()

result_label = tk.Label(window, text="")
result_label.pack()

def tinh_toan():
    distance = float(khoang_cach.get())
    fare = 12000  
    if distance > 0.8:
        if distance <= 30:
            fare += (distance - 0.8) * 15300
        else:
            fare += (30 - 0.8) * 15300 + (distance - 30) * 12100
    result_label.config(text=f"Total Fare: {fare} VND")

tk.Button(window, text="Tính toán", command=tinh_toan).pack()

window.mainloop()
