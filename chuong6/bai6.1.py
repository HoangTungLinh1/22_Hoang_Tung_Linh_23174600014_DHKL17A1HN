import threading

def print_thread_name():
    print(f"Thread Name: {threading.current_thread().name}")

n=int(input("Nhập số luồng muốn hiển thị: "))
threads = []
for i in range(n):
    thread = threading.Thread(target=print_thread_name, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
