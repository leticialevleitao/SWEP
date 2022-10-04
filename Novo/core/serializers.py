from rest_framework import serializers
from core.models import User, Receitas, Indicacoes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'usuario', 'email', 'senha', 'regiao']

class ReceitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = ['titulo', 'ingredientes', 'descricao']

class IndicacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicacoes
        fields = ['descricao2', 'tipo']
