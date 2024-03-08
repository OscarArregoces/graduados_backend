from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.application.auth_module.api.serializers.carrera.carrera_serializers import CarreraSerializers
from src.application.auth_module.api.serializers.person.persons_serializers import PersonsCreateSerializer, PersonsDetailSerializers
from src.application.auth_module.models import Carrera, Persons, User

class CarreraView(APIView):
    
    def get_instance(self, person_id):
        try:
            return Persons.objects.get(id=person_id)
        except Persons.DoesNotExist:
            return None
    def get(self, request, *args, **kwargs):
        try:
            usuario_id = request.user.id
            user =  get_object_or_404(User, id=usuario_id)
            
            persona = user.person
            if persona is None:
                return Response("La persona asociada al usuario no existe.", status=404)
            
            carreras = Carrera.objects.filter(person=persona)
            carrera_serializer = CarreraSerializers(carreras, many=True)
            persona_serializer = PersonsDetailSerializers(persona)
            
            return Response({
                "persona": persona_serializer.data,
                "carreras": carrera_serializer.data
                }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        persona_id = kwargs.get("persona_id", None)
        
        if persona_id is None:
            return Response({"error":"id es requerido"},status=status.HTTP_400_BAD_REQUEST)
        
        person = self.get_instance(persona_id)
        if person is None:
            return Response({"error":"persona no encontrada"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonsCreateSerializer(person, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

       