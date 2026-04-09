from django.db import models
from apps.profesor.models import Profesor
from apps.alumno.models import Alumno

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    profesores = models.ManyToManyField(Profesor)
    alumnos = models.ManyToManyField(Alumno)
    def __str__(self):
        return self.nombre