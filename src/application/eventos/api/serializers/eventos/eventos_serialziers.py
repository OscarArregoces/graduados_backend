from rest_framework import serializers
from configs.middlewares.auth import User
from src.application.auth_module.api.serializers.gestor.gestor_serializer import GestorSerializer
from src.application.auth_module.api.serializers.head_serializers import HeadSerializers
from src.application.auth_module.api.serializers.user.users_serializers import UserCreatedSerializer
from src.application.eventos.api.serializers.eventos.eventosStatus_serializers import EventosStatusSerializers
from src.application.eventos.api.serializers.eventos.eventos_cate_serializers import EventosCategorySerializersView
from src.application.eventos.api.serializers.eventos.eventos_servicios_serializer import ServiciosSerializersView
from src.application.eventos.api.serializers.eventos.eventos_sub_area_serializers import  SubAreaSimpleSerializer
from src.application.eventos.api.serializers.eventos.eventos_tipo import TipoEventosSerializersView

from src.application.eventos.models.models import Eventos, Servicios


class EventosSerializer(serializers.ModelSerializer):
    area = EventosCategorySerializersView(read_only=True)
    subarea = SubAreaSimpleSerializer(read_only=True)
    tipo_actividad = TipoEventosSerializersView(read_only=True)
    servicios = ServiciosSerializersView(many=True, read_only=True)
    dependencia = GestorSerializer(read_only=True)
    sede = HeadSerializers(read_only=True)
    userCreate = UserCreatedSerializer(read_only=True)
    estado_actividad = EventosStatusSerializers(read_only=True)
    
    class Meta:
        model = Eventos
        exclude = ( "userUpdate", "name","createdAt","updateAt", "visible")
        
class EventosSimpleSerializer(serializers.ModelSerializer):
    # tipo_actividad = TipoEventosSerializersView(read_only=True)
    # dependencia = GestorSerializer(read_only=True)
    # sede = HeadSerializers(read_only=True)
    # estado_actividad = EventosStatusSerializers(read_only=True)
    
    class Meta:
        model = Eventos
        fields = ( "id","nombre_actividad",)
        # fields = ( "id","nombre_actividad", "tipo_actividad", "dependencia", "sede", "modalidad")
        
class EventosCreateSerializer(serializers.ModelSerializer):
    servicios = serializers.PrimaryKeyRelatedField(many=True, queryset=Servicios.objects.all())
    class Meta:
        model = Eventos
        fields = '__all__'

# class EventosAprobacionCreateSerializer(serializers.ModelSerializer):
#     servicios = serializers.PrimaryKeyRelatedField(many=True, queryset=Servicios.objects.all())
#     class Meta:
#         model = Eventos
#         fields = '__all__'
        