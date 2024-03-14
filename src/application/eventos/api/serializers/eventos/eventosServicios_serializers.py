from src.application.eventos.models.models import Eventos, EventosServicios
from rest_framework import serializers

class EventosServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventosServicios
        fields = '__all__'
