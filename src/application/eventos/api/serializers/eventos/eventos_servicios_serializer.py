from rest_framework.serializers import ModelSerializer
from src.application.eventos.models.models import Servicios

class ServiciosSerializersView(ModelSerializer):
    class Meta:
        model = Servicios
        fields = ("id","name")