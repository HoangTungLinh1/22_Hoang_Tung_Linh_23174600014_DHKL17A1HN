import pandas as pd

# Tạo Series chứa chuỗi ngày
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

# Chuyển đổi chuỗi ngày thành chuỗi thời gian với dayfirst=True để đảm bảo pandas hiểu đúng định dạng ngày
ser_datetime = pd.to_datetime(ser, dayfirst=True, errors='coerce')

# Hiển thị kết quả
print(ser_datetime)
