from tkinter import *
window = Tk()
window.title("Welcome to Uneti.")

lbl = Label(window, text="Hello")

window.geometry('280x80')

lbl.grid(column=0, row=0)

window.mainloop()