import json

from requests import post

url = "http://127.0.0.1:8000/api/v1/editar_estudante/12/"

payload = {
    "nome": "Frigida",
    "serie": "5ª Ensino Fund",
    "data_nascimento": "2000-04-15",
    "sexo": "F"
}

headers = {'Content-Type': 'text/plain'}

payload = json.dumps(payload, separators=(',', ':'))

response = post(url, headers=headers, data=payload)

print(response.text)
