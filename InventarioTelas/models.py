from django.conf import settings
from django.db import models
from django.utils import timezone

class Tela(models.Model):
    titulo = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='telas',default='FotoTela')
    tejido = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    localizacion = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.titulo