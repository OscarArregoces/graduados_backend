from responses import Response
from src.application.auth_module.api.serializers.gestor.gestor_serializer import GestorSerializer
from src.application.auth_module.models import Gestor
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class GestorView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            gestores = Gestor.objects.all() 
            gestores_serializer = GestorSerializer(gestores, many=True)
            return Response(gestores_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)