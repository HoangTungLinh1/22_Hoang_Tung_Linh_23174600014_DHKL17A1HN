import requests

response = requests.get("https://jsonplaceholder.typicode.com/comments?postId=1")
    
if response.status_code == 200:
    posts = response.json()

    print(f"Tổng số bài post nổi bật: {len(posts)}\n")
        
    for post in posts[:3]:
        print(f"PostID: {post['postId']}")
        print(f"ID: {post['id']}")
        print(f"Name: {post['name']}")
        print(f"Email: {post['email']}")
        print(f"Body: {post['body']}")
        print("===============================")
else:
    print("Không thể lấy dữ liệu từ API. Mã lỗi:", response.status_code)


