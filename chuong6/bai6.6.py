import threading

lock = threading.Lock()
dem = 0

def print_even(gia_tri_max):
    global dem
    while dem <= gia_tri_max:
        with lock:
            if dem % 2 == 0:
                print(f"Chẵn: {dem}")
                dem += 1

def print_odd(gia_tri_max):
    global dem
    while dem <= gia_tri_max:
        with lock:
            if dem % 2 != 0:
                print(f"Lẻ: {dem}")
                dem += 1

gia_tri_max = 10
thread1 = threading.Thread(target=print_even, args=(gia_tri_max,))
thread2 = threading.Thread(target=print_odd, args=(gia_tri_max,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
