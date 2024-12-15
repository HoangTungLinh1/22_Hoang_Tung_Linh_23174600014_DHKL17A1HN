import threading
import time

def download_file(file_name):
    print(f"Downloading {file_name}...")
    time.sleep(2)  
    print(f"Finished downloading {file_name}")

file_names = ["file1.txt", "file2.txt", "file3.txt"]
threads = []
for file in file_names:
    thread = threading.Thread(target=download_file, args=(file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
