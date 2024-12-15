import threading

def factorial_part(start, end, result, index):
    temp = 1
    for i in range(start, end+1):
        temp *= i
    result[index] = temp

n = int(input("nhập số muốn tính giai thừa: "))
num_threads = 2
step = n // num_threads
threads = []
results = [1] * num_threads

for i in range(num_threads):
    start = i * step + 1
    end = n if i == num_threads - 1 else (i + 1) * step
    thread = threading.Thread(target=factorial_part, args=(start, end, results, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

giai_thua = 1
for res in results:
    giai_thua *= res

print(f"giai thừa của {n} la {giai_thua}")
