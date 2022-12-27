from django.db import models

class familiares(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    estado_civil = models.BooleanField()
