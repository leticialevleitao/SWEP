from rest_framework import viewsets
from be_drf.models import User, Recipe
from be_drf.serializers import UserSerializer, RecipeSerializer

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

