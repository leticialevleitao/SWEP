from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    email = models.EmailField(blank=False, max_length=100, default=None)
    password = models.CharField(max_length=100)
    region = models.CharField(max_length=20)

    def str(self):
        return self.name

class Receitas(models.Model):
    titulo = models.CharField(max_length=50)
    ingredientes = models.CharField(max_length=300)
    descricao = models.TextField()

    def str(self):
        return self.titulo

class Indicacoes(models.Model):
    descricao2 = models.TextField()
    tipo = models.CharField(max_length=50)

    def str(self):
        return self.decricao2

