from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Proyectos(models.Model):
    url_foto = models.CharField(max_length=300, default="")
    proyecto = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=600)
    tags = models.ForeignKey(Tags, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    github = models.CharField(max_length=200)

class Visitantes(models.Model):
    ip = models.CharField(max_length=50)
    momento_registrado = models.DateTimeField(auto_now_add=True, null=True)
