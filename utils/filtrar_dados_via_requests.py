import json

from requests import get

url = "http://127.0.0.1:8000/api/v1/filtar_estudante/"

# payload = {"nome": "e"}
# payload = {"sexo": "F"}
payload = {"data_nascimento": "08/06/2005"}

headers = {'Content-Type': 'application/json'}

payload = json.dumps(payload, separators=(',', ':'))

response = get(url, data=payload, headers=headers)

print(response.json())

