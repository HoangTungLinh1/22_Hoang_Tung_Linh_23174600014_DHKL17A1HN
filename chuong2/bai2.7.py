import json

json_string='{"name":"Nguyen Van A", "age": 18}'

json_object=json.loads(json_string)

print(json_object)