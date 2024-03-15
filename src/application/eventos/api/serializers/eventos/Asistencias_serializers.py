from attr import fields
from rest_framework import serializers

from src.application.auth_module.api.serializers.user.users_serializers import UserAsistenciaSerializer, UserPonentesSerializer
from src.application.eventos.models.models import Asistencia, AsistenciaExternos

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Asistencia
        fields = ("id","actividad","user","confirmacion","asistencia")
        read_only_fields = fields
        
class AsistenciarReporteSerializer(serializers.ModelSerializer):
    user = UserAsistenciaSerializer(read_only=True)
    class Meta: 
        model = Asistencia
        fields = ("user","confirmacion","asistencia")
        read_only_fields = fields
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user_representation = representation.pop("user", None)
        if user_representation:
            person_representation = user_representation.get("person", None)
            if person_representation:
                representation.update(person_representation)
                representation.pop("person", None)
        return representation
        
class AsistenciaReporteExternosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = AsistenciaExternos
        fields = ("fullname" ,"email", "phone")
        read_only_fields = fields


class AsistenciaCreateSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = Asistencia
        fields = "__all__"
class AsistenciaExternoCreateSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = AsistenciaExternos
        fields = "__all__"