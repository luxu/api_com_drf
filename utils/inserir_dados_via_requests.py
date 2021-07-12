import json

from requests import post

url = "http://127.0.0.1:8000/api/v1/novo_estudante/"
payload = {"nome": "Beltrara",
            "serie": "6ª Ensino Fund",
            "data_nascimento": "2008-02-15",
            "sexo": "F"
        }
headers = {'Content-Type': 'text/plain'}

payload = json.dumps(payload, separators=(',', ':'))
response = post(url, headers=headers, data=payload)

print(response.text)
