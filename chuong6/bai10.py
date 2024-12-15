import threading
import random

def partial_max(sub_list, result, index):
    result[index] = max(sub_list)

n = 20
du_lieu = [random.randint(0, 100) for _ in range(n)]
so_thread = 4
kich_thuoc = n // so_thread

threads = []
ket_qua = [0] * so_thread

for i in range(so_thread):
    start = i * kich_thuoc
    end = n if i == so_thread - 1 else (i + 1) * kich_thuoc
    thread = threading.Thread(target=partial_max, args=(du_lieu[start:end], ket_qua, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"danh sách: {du_lieu}")
print(f"giá trị max: {max(ket_qua)}")
