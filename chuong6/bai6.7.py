import threading
import time
from datetime import datetime

def web_access(ten_web, thoi_gian, khoang_tg):
    print(f"Starting {ten_web}")
    for i in range(khoang_tg):
        tg_gan_nhat = datetime.now().strftime("%b %d %H:%M:%S %Y")
        print(f"{ten_web}: Web {tg_gan_nhat}")
        time.sleep(thoi_gian)  
    print(f"Exiting {ten_web}")

def main():
    threads = []
    thread_data = [
        ("Google", 1, 4),    
        ("Yahoo", 2, 3),     
        ("Facebook", 3, 3)   
    ]


    for ten_web, thoi_gian, khoang_tg in thread_data:
        thread = threading.Thread(target=web_access, args=(ten_web, thoi_gian, khoang_tg))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Exiting Main Thread")

if __name__ == "__main__":
    main()
