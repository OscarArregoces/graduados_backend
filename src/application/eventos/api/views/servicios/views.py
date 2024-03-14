
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.application.eventos.api.serializers.eventos.eventos_servicios_serializer import ServiciosSerializersView

from src.application.eventos.models.models import Servicios

class ServiciosView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            servicios = Servicios.objects.all()
            serializer = ServiciosSerializersView(servicios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    


       