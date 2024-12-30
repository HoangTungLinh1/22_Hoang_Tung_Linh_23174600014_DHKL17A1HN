import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import requests
from io import BytesIO

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[
        ("All Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"),
        ("PNG Files", "*.png"),
        ("JPEG Files", "*.jpg;*.jpeg"),
        ("BMP Files", "*.bmp"),
        ("GIF Files", "*.gif")
    ])
    if file_path:
        display_image(file_path)

def load_image_from_url():
    url = url_entry.get()
    try:
        response = requests.get(url)
        response.raise_for_status()
        img_data = BytesIO(response.content)
        display_image(img_data)
    except Exception as e:
        print(f"Lỗi khi tải ảnh từ URL: {e}")

def display_image(image_source):
    try:
        img = Image.open(image_source)
        img = img.resize((300, 200), Image.LANCZOS)  
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    except Exception as e:
        print(f"Lỗi khi hiển thị ảnh: {e}")

window = tk.Tk()
window.title("Hiển Thị Ảnh")
window.geometry("400x400")

tk.Button(window, text="Chọn Ảnh Từ File", command=open_image).place(x=50, y=50, width=150)

tk.Label(window, text="Nhập URL Ảnh:").place(x=50, y=100)
url_entry = tk.Entry(window)
url_entry.place(x=50, y=130, width=300)

tk.Button(window, text="Tải Ảnh Từ URL", command=load_image_from_url).place(x=50, y=170, width=150)

image_label = tk.Label(window)
image_label.place(x=50, y=210, width=300, height=200)

window.mainloop()

window.mainloop()
