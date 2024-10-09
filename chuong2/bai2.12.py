import requests

response =requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code==200:
    json_data=response.json()

    for post in json_data:
        print("ID bài đăng:", post['id'])
        print("Tiêu đề:", post['title'])
        print("Nội dung", post['body'])
        print("===============================")
else:
    print("Yêu cầu không thành công. Mã trạng thái:", response.status_code)