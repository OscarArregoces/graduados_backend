from attr import fields
from rest_framework import serializers

from src.application.eventos.models.models import Asistencia

class AsistenciaSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Asistencia
        fields = ("id","actividad","user","confirmacion","asistencia")
        read_only_fields = fields