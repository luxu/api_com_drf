# API com DRF

### Como rodar o projeto
* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
````
git clone https://github.com/luxu/api_com_drf
cd api_com_drf
python -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python importando_estudantes.py
````

## endpoints

* lista os estudantes ```` api/v1/listar_estudantes/ ````
* detalhe do estudante ```` api/v1/detalhe_estudante/5/````
* novo estudante ```` api/v1/novo_estudante/````
* edita o estudante ```` api/v1/editar_estudante/7/````
* deleta o estudante ```` api/v1/apagar_estudante/7/````
* busca pelo critério ```` api/v1/filtar_estudante/ (por nome, por data_nascimento, por sexo)````


Buscas:
````
por nome -> entrar com parte do nome
por sexo
por data_nascimento -> traz os nascidos ACIMA da data passada
````