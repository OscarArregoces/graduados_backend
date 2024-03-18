
from rest_framework import serializers
from src.application.eventos.models.models import Evidencias


class EvidenciasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidencias
        fields = ("id","actividad","titulo","archivo")
        read_only_fields = fields
        
class EvidenciasCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidencias
        fields = "__all__"