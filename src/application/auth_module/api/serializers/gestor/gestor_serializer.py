from rest_framework import serializers
from src.application.auth_module.models import Gestor

class GestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestor
        fields = ('id','name')