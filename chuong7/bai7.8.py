import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("400x250")

label = tk.Label(window, text="Enter value of N:")
label.pack()

entry = tk.Entry(window)
entry.pack()

result_label = tk.Label(window, text="")
result_label.pack()

def validate():
    N = int(entry.get())
    divisors = [str(i) for i in range(1, N+1) if N % i == 0]
    result_label.config(text="The divisors of N: " + " ".join(divisors))

button = tk.Button(window, text="Validate", command=validate)
button.pack()

window.mainloop()
