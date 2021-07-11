from datetime import datetime

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from secretaria.models import Estudante
from secretaria.serializer import EstudanteSerializer


@api_view(['GET'])
def estudantes_list(request):
    estudantes = Estudante.objects.all()
    estudantes_serializer = EstudanteSerializer(estudantes, many=True)
    return JsonResponse(estudantes_serializer.data, safe=False)


@api_view(['GET'])
def estudantes_details(request, pk):
    try:
        estudante = Estudante.objects.get(id=pk)
    except Estudante.DoesNotExist:
        return JsonResponse(
            {
                'message': 'Estudante não existe!'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    estudante_serializer = EstudanteSerializer(estudante)
    return JsonResponse(estudante_serializer.data, safe=False)


@api_view(['POST'])
def estudante_create(request):
    estudante_data = JSONParser().parse(request)

    estudantes_serializer = EstudanteSerializer(data=estudante_data)
    if estudantes_serializer.is_valid():
        estudantes_serializer.save()
        return JsonResponse(estudantes_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(estudantes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def estudante_edit(request, pk):
    try:
        estudantes = Estudante.objects.get(id=pk)
    except Estudante.DoesNotExist:
        return JsonResponse(
            {
                'message': 'Estudante não existe!'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    estudante_data = JSONParser().parse(request)
    estudantes_serializer = EstudanteSerializer(estudantes, data=estudante_data)
    if estudantes_serializer.is_valid():
        estudantes_serializer.save()
        return JsonResponse(estudantes_serializer.data)
    return JsonResponse(estudantes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def estudante_delete(request, pk):
    try:
        estudantes = Estudante.objects.get(id=pk)
    except Estudante.DoesNotExist:
        return JsonResponse(
            {
                'message': 'Estudante não existe!'
            },
            status=status.HTTP_404_NOT_FOUND
        )
    nome = estudantes.nome
    estudantes.delete()
    return JsonResponse(
        {
            'message': f'O estudante: {nome} foi apagado com sucesso!'
        },
        status=status.HTTP_204_NO_CONTENT
    )


@api_view(['GET'])
def estudante_filter(request):
    estudante_data = JSONParser().parse(request)
    try:
        nome = estudante_data['nome']
        estudantes = Estudante.objects.filter(nome__contains=nome)
    except KeyError:
        nome = ''
    try:
        sexo = estudante_data['sexo']
        estudantes = Estudante.objects.filter(sexo=sexo)
    except KeyError:
        sexo = ''
    try:
        data_nascimento = estudante_data['data_nascimento']
        dia, mes, ano = data_nascimento.split('/')
        dt = datetime(int(ano), int(mes), int(dia))
        estudantes = Estudante.objects.filter(data_nascimento__gte=dt)
    except KeyError:
        data_nascimento = ''
    estudantes_serializer = EstudanteSerializer(estudantes, many=True)
    return JsonResponse(estudantes_serializer.data, safe=False)
