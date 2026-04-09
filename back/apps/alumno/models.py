from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.codigo