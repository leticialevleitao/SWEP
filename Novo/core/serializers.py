from rest_framework import serializers
from core.models import User, Receitas, Indicacoes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'nick_name', 'email', 'password', 'region']

class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = ['titulo', 'ingredientes', 'descricao']

class IndicacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicacoes
        fields = ['descricao2', 'tipo']
