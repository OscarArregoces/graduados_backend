from rest_framework import serializers
from src.application.auth_module.api.serializers.user.users_serializers import UserPonentesSerializer, UserSerializers
from src.application.eventos.models.models import Eventos, PonentesExternos, PonentesVinculacion

class PonentesVinculacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PonentesVinculacion
        fields = '__all__'

class PonentesExternosCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PonentesExternos
        fields = '__all__'
        
class PonentesVinculacionSerializerView(serializers.Serializer):
    # actividad = serializers.IntegerField(read_only=True)
    user = UserPonentesSerializer()
    rol = serializers.CharField(read_only=True)
    vinculacion = serializers.CharField(read_only=True)
    dedicacion = serializers.CharField(read_only=True)
    
    def to_representation(self, instance):
        data = super(PonentesVinculacionSerializerView, self).to_representation(instance)
        data['user'] = data['user']['person']
        return data
    
class PonentesExternosSerializerVew(serializers.Serializer):
    # actividad = serializers.IntegerField(read_only=True)
    dedicacion = serializers.CharField(read_only=True)
    document = serializers.CharField(read_only=True)
    email = serializers.CharField(read_only=True)
    fullname = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    rol = serializers.CharField(read_only=True)
    vinculacion = serializers.CharField(read_only=True)