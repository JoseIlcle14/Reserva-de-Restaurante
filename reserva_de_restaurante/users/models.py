from django.db import models
from django.core.validators import MinLengthValidator

class Usuários(models.Model):

    nome = models.CharField(max_length= 200)
    cpf = models.CharField(
        max_length= 11,
        validators= [MinLengthValidator(11)]
    )
    email = models.EmailField(max_length=128)
    senha = models.CharField(
        max_length= 128,
        validators =[MinLengthValidator(8)]
    )
