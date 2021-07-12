from requests import get

url = "http://127.0.0.1:8000/api/v1/detalhe_estudante/11/"

headers = {'Content-Type': 'application/json'}

response = get(url).json()

print(response)
