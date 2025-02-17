import numpy as np

arr = np.full((3, 3), True)
print("Mảng 3x3 với các giá trị True:")
print(arr)

arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])  

arr_2D = arr_ID.reshape(3, 3)
print("\nArray 2D ban đầu:")
print(arr_2D)

arr_2D[:, [1, 2]] = arr_2D[:, [2, 1]]
print("\nArray 2D sau khi đổi chỗ cột 1 và cột 3:")
print(arr_2D)

arr_2D[[0, 1]] = arr_2D[[1, 0]]
print("\nArray 2D sau khi đổi chỗ dòng 1 và dòng 2:")
print(arr_2D)

arr_2D = arr_2D[::-1]
print("\nArray 2D sau khi đảo ngược các dòng:")
print(arr_2D)

arr_2D = arr_2D[:, ::-1]
print("\nArray 2D sau khi đảo ngược các cột:")
print(arr_2D)

arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("\nCó giá trị NaN trong arr_2D_null:", has_nan)

arr_2D_null[np.isnan(arr_2D_null)] = 0
print("\nArray 2D null sau khi thay thế NaN bằng 0:")
print(arr_2D_null)
