import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage


con_giap = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]


anh_con_giap = {
    "Tý": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\chuot.jpg", 
    "Sửu": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\trau.jpg",
    "Dần": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\ho.jpg",
    "Mão": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\tho.jpg",
    "Thìn": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\rong.jpg",
    "Tỵ": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\ran.jpg",
    "Ngọ": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\ngua.jpg",
    "Mùi": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\de.jpg",
    "Thân": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\khi.jpg",
    "Dậu": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\ga.png",
    "Tuất": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\cho.png",
    "Hợi": r"D:\BT_python_nang_cao\Hoang_Tung_Linh_23174600014_DHKL17A1HN\lon.jpg"
}

def get_zodiac_year():
    year_str = year_entry.get()

    if not year_str.isdigit():
        messagebox.showerror("Lỗi", "Vui lòng nhập một năm hợp lệ.")
        return
    
    year = int(year_str)

    zodiac_year = con_giap[(year - 4) % 12]

    result_label.config(text=f"Năm {year} Dương lịch là năm {zodiac_year} Âm lịch")

    img = PhotoImage(file=anh_con_giap[zodiac_year])
    img_label.config(image=img)
    img_label.image = img

window = tk.Tk()
window.title("Chuyển đổi Năm Dương lịch sang Âm lịch")
window.geometry("400x450")

tk.Label(window, text="Nhập năm Dương lịch:").pack(pady=10)

year_entry = tk.Entry(window)
year_entry.pack(pady=5)

convert_button = tk.Button(window, text="Chuyển đổi", command=get_zodiac_year)
convert_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

img_label = tk.Label(window)
img_label.pack(pady=10)

window.mainloop()
