from django.db import models

# Create your models here.


class Cadastrer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    senha = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = 'Formulario de contato'
    verobose_name_plural = 'Formularios de contatos'
    ordering = ['-data']