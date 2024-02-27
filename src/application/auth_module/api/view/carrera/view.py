from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.application.auth_module.api.serializers.carrera.carrera_serializers import CarreraSerializers
from src.application.auth_module.api.serializers.person.persons_serializers import PersonsSerializer, PersonsSerializers, PersonsSimpleSerializersView, UsuariosExcelSerializersView
from src.application.auth_module.api.serializers.user.users_serializers import UserSerializers

from src.application.auth_module.models import Carrera, Persons, User

class CarreraView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            
            usuario_id = request.user.id
            user =  get_object_or_404(User, id=usuario_id)
            
            persona = user.person
            if persona is None:
                return Response("La persona asociada al usuario no existe.", status=404)
            
            carreras = Carrera.objects.filter(person=persona)
            carrera_serializer = CarreraSerializers(carreras, many=True)
            persona_serializer = PersonsSerializers(persona)
            
            return Response({
                "persona": persona_serializer.data,
                "carreras": carrera_serializer.data
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)