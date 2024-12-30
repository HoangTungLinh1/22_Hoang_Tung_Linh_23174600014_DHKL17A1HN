import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("300x200")

def reverse_word():
    word = entry.get()  
    reversed_word = "".join([word[i] for i in range(len(word)-1, -1, -1)])  
    result_label.config(text=reversed_word)

tk.Label(window, text="Enter a word:").place(x=50, y=10)

entry = tk.Entry(window)
entry.place(x=50, y=40, width=200)

tk.Button(window, text="Validate", command=reverse_word).place(x=100, y=100)

result_label = tk.Label(window, text="")
result_label.place(x=50, y=60)

window.mainloop()
