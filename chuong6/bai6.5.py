import threading
import requests

def fetch_url(url):
    response = requests.get(url)
    print(f"{url}: Status {response.status_code}")

urls = ["https://google.com", "https://yahoo.com", "https://facebook.com"]
threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
