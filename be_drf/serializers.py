from rest_framework import serializers
from be_drf.models import User, Recipe, Indicacoes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'nick_name', 'email', 'password', 'region']

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['titulo', 'ingredientes', 'description']

class IndicacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicacoes
        fields = ['description2', 'tipo']
