import csv
import os
from datetime import datetime

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
django.setup()

from secretaria.models import Estudante


def csv_to_list(filename: str) -> list:
    '''Lê um csv e retorna um OrderedDict.
    Créditos para Rafael Henrique
    https://bit.ly/2FLDHsH
    '''
    with open(filename, encoding='UTF8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        csv_data = [line for line in reader]
    return csv_data


def save_data(data):
    '''Salva os dados no banco.'''
    aux = []
    for item in data:
        nome = item.get('nome')
        data_nascimento = item.get('data_nascimento')
        dia, mes, ano = data_nascimento.split('/')
        data_nascimento = datetime(int(ano), int(mes), int(dia))
        sexo = str(item.get('sexo'))
        serie = str(item.get('serie'))
        obj = Estudante(
            nome=nome,
            data_nascimento=data_nascimento,
            serie=serie,
            sexo=sexo
        )
        aux.append(obj)
    Estudante.objects.bulk_create(aux)


data = csv_to_list('fix/estudantes.csv')
save_data(data)
