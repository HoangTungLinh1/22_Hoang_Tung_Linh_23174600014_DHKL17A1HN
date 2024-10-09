import json

du_lieu={"name": "Nguyen Van A",
         "age": 18,
         "city": "Ha Noi"}

sap_sep_dl=dict(sorted(du_lieu.items()))

json_string=json.dumps(sap_sep_dl, indent=4, ensure_ascii=False)

print(json_string)