import threading
import random

def partial_sum(sub_list, result, index):
    result[index] = sum(sub_list)

n = 20
data = [random.randint(0, 10) for _ in range(n)]
num_threads = 4
chunk_size = n // num_threads

threads = []
results = [0] * num_threads

for i in range(num_threads):
    start = i * chunk_size
    end = n if i == num_threads - 1 else (i + 1) * chunk_size
    thread = threading.Thread(target=partial_sum, args=(data[start:end], results, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"List: {data}")
print(f"Total Sum: {sum(results)}")
