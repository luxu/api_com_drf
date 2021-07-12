from django.db import models

from secretaria import constants


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    serie = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=constants.SEXO)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['-id']
