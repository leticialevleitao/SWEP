from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserSwep(AbstractUser):
    idade = models.IntegerField(null=True, blank=True)


class Recipe(models.Model):
    titulo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=300)
    description = models.TextField()

    def str(self):
        return self.titulo

class Indicacoes(models.Model):
    description2 = models.TextField()
    tipo = models.CharField(max_length=50)

    def str(self):
        return self.decription2
