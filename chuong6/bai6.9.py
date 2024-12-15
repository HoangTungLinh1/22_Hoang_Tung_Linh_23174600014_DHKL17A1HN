import threading
import time
import random

def web_access(name):
    print(f"Starting {name}: Web Access at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    time.sleep(random.randint(1, 3))  
    print(f"Exiting {name}: Web Access at {time.strftime('%Y-%m-%d %H:%M:%S')}")

websites = ["Google", "Yahoo", "Facebook"]

threads = []

for site in websites:
    thread = threading.Thread(target=web_access, args=(site,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

