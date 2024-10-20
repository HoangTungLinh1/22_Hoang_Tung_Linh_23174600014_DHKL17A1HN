import numpy as np

arr_zeros = np.zeros(10, dtype=int)
arr_zeros[4] = 1  
print("arr_zeros:", arr_zeros)

arr_h = np.arange(10, 25)
print("arr_h:", arr_h[::-1])

arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_1 = arr_k[arr_k != 0]
print("arr_1:", arr_1)

arr_1 = np.append(arr_1, [10, 20])
print("arr_1", arr_1)

arr_1 = np.insert(arr_1, 5, 100)
print("arr_1:", arr_1)

arr_1 = np.delete(arr_1, [0, 1, 2])
print("arr_1:", arr_1)
