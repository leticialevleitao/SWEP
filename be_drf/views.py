from rest_framework import viewsets
from be_drf.models import User, Recipe, Indicacoes
from be_drf.serializers import UserSerializer, RecipeSerializer, IndicacoesSerializer

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
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

class IndicacoesViewSet(viewsets.ModelViewSet):
    """
    Showing Each Indication
    """
    queryset = Indicacoes.objects.all()
    serializer_class = IndicacoesSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

