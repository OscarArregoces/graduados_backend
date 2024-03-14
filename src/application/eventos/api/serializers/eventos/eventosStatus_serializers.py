from rest_framework import serializers

from src.application.eventos.models.models import EventosStatus


class EventosStatusSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = EventosStatus
        fields = ("id","name")
        read_only_fields = fields