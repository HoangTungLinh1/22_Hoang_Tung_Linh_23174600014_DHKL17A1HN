import json

du_lieu={
    "name": "Nguyen Van A",
    "age": 18
}

json_string=json.dumps(du_lieu, ensure_ascii=False)

print(json_string)