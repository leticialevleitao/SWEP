from django.shortcuts import render
from rest_framework import viewsets
from core.models import User, Receitas, Indicacoes
from core.serializers import UserSerializer, ReceitasSerializer, IndicacoesSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """
    Showing Each User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'patch']

class RecipesViewSet(viewsets.ModelViewSet):
    """
    Showing Each Recipe
    """
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

class IndicacoesViewSet(viewsets.ModelViewSet):
    """
    Showing Each Indication
    """
    queryset = Indicacoes.objects.all()
    serializer_class = IndicacoesSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
