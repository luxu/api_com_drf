# API com DRF

### Como rodar o projeto
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
````
git clone https://github.com/luxu/api_com_drf
````
````
cd api_com_drf
````
````
python -m virtualenv .venv
````
````
source .venv/bin/activate
````
````
python -m pip install --upgrade pip
````
````
pip install -r requirements.txt
````
````
python contrib/env_gen.py
````
````
python manage.py migrate
````
````
python importando_estudantes.py
````

## endpoints

* lista os estudantes ```` api/v1/listar_estudantes/ ````
* detalhe do estudante ```` api/v1/detalhe_estudante/<id>/````
* novo estudante ```` api/v1/novo_estudante/````
* edita o estudante ```` api/v1/editar_estudante/<id>/````
* deleta o estudante ```` api/v1/apagar_estudante/<id>/````
* busca pelo critério ```` api/v1/filtar_estudante/ (por nome, por data_nascimento, por sexo)````


## Versão online rodando no Heroku
https://api-com-drf.herokuapp.com/api/v1/listar_estudantes

## Para listar os estudantes
````
import json
from requests import get

url = "http://127.0.0.1:8000/api/v1/listar_estudantes/"

headers = {'Content-Type': 'application/json'}

response = get(url).json()

print(response)

````

## Para adicionar estudante
````
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
````

## Para editar estudante
````
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

````

## Para detalhar estudante
````
from requests import get

url = "http://127.0.0.1:8000/api/v1/detalhe_estudante/11/"

headers = {'Content-Type': 'application/json'}

response = get(url).json()

print(response)
````

## Para deletar estudante
````
import json

from requests import delete

url = "http://127.0.0.1:8000/api/v1/apagar_estudante/12/"

headers = {'Content-Type': 'text/plain'}

response = delete(url)

print(response.text)

````

## Para filtar estudantes
````
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

````

### Buscas:
````
por nome -> entrar com parte do nome
por data_nascimento -> traz os nascidos ACIMA da data passada
por sexo
````