import numpy as np

arr=np.arange(10)
print(arr)

print("Kiểu dữ liệu:", arr.dtype)
print("kích thước:", arr.shape)

arr_odd = arr[arr % 2 !=0]
arr_even=arr[arr % 2==0]
print("Mảng các phần tử lẻ:", arr_odd)
print("Mảng các phần tử chẵn:", arr_even)

arr_update_1=np.where(arr%2==0, arr, 100)
print("Mảng cập nhật:", arr_update_1)