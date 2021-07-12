import json

from requests import delete

url = "http://127.0.0.1:8000/api/v1/apagar_estudante/12/"

headers = {'Content-Type': 'text/plain'}

response = delete(url)

print(response.text)
