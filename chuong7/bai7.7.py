import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("400x250")

tk.Label(window, text="Enter value of integer N:").place(x=50, y=30)

entry = tk.Entry(window)
entry.place(x=50, y=60, width=200)

tk.Button(window, text="Validate", command=lambda: 
          result_label.config(text=f"The sum is {' + '.join(map(str, range(1, int(entry.get()) + 1)))} = {sum(range(1, int(entry.get()) + 1))}" 
          if entry.get().isdigit() and int(entry.get()) > 0 else "Vui lòng nhập số nguyên hợp lệ!")).place(x=150, y=100)

result_label = tk.Label(window, text="")
result_label.place(x=50, y=80)

window.mainloop()
