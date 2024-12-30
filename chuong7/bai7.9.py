import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.title("GCD and LCM Calculator")
window.geometry("400x250")

tk.Label(window, text="Enter value of m:").pack()
entry_m = tk.Entry(window)
entry_m.pack()

tk.Label(window, text="Enter value of n:").pack()
entry_n = tk.Entry(window)
entry_n.pack()

tk.Label(window, text="Choose function:").pack()
function_var = tk.StringVar()
function_combobox = ttk.Combobox(window, textvariable=function_var, state="readonly")
function_combobox['values'] = ("GCD", "LCM")
function_combobox.current(0)  
function_combobox.pack()

result_label = tk.Label(window, text="")
result_label.pack()

def tinh_toan():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())
        choice = function_var.get()
        
        if choice == "GCD":
            result = math.gcd(m, n)
            result_label.config(text=f"GCD({m}, {n}) = {result}")
        elif choice == "LCM":
            result = (m * n) // math.gcd(m, n)
            result_label.config(text=f"LCM({m}, {n}) = {result}")
    except ValueError:
        result_label.config(text="Please enter valid integers!")

tinh_toan_button = tk.Button(window, text="tinh_toan", command=tinh_toan)
tinh_toan_button.pack()

window.mainloop()
