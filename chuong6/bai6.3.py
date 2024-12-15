import threading

def tim_so_chan(start, end):
    print(f"số chẵn: {[n for n in range(start, end+1) if n % 2 == 0]}")

def tim_so_le(start, end):
    print(f"số lẻ: {[n for n in range(start, end+1) if n % 2 != 0]}")

thread1 = threading.Thread(target=tim_so_chan, args=(30, 50))
thread2 = threading.Thread(target=tim_so_le, args=(30, 50))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
