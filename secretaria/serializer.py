from rest_framework import serializers
from secretaria.models import Estudante


class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'
