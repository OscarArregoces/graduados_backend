from django.utils import timezone
from rest_framework.views import APIView   

from rest_framework.response import Response
from rest_framework import status

from src.application.eventos.api.serializers.eventos.Evidencias_serializers import EvidenciasCreateSerializer, EvidenciasSerializer
from src.application.eventos.models.models import Eventos, Evidencias

from rest_framework.parsers import MultiPartParser, FormParser
import json

class EvidenciasView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id',None)
        if actividad_id is None:
            return Response({'errors': 'actividad_id es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            evidencias = Evidencias.objects.filter(actividad=actividad_id)
            evidencias_serializer = EvidenciasSerializer(evidencias, many=True)
            return Response(evidencias_serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
  
    def post(self, request, *args, **kwargs):
        try:
            actividad_id = kwargs.get('actividad_id',None)
     
            actividad = Eventos.objects.filter(id=actividad_id).first()
            
            if actividad is None:
                return Response({"error": "Actividad no existe"}, status=status.HTTP_404_NOT_FOUND)
            
            archivos = request.FILES.getlist('archivos') 
            titulos = request.POST.getlist('titulos')
            archivos_sin_cambios_json = request.POST.get('archivosSinCambios')
            archivos_sin_cambios = json.loads(archivos_sin_cambios_json)
            
            if((len(archivos_sin_cambios) + len(archivos)) > 4):
                return Response({"error": "No puedes cargar mas de 5 archivos"}, status=status.HTTP_400_BAD_REQUEST)
            
            if len(archivos) != len(titulos):
                return Response({"error": "La cantidad de archivos y títulos no coincide"}, status=status.HTTP_400_BAD_REQUEST)

            evidencias = Evidencias.objects.filter(actividad_id=actividad_id)
            
            for evidencia in evidencias:
                if evidencia.archivo in [archivo['archivo'] for archivo in archivos_sin_cambios]:
                    evidencia.delete()
            
            for archivo, titulo in zip(archivos, titulos):
                evidencia_serializer = EvidenciasCreateSerializer(data={'actividad': actividad_id, 'titulo': titulo, 'archivo': archivo})
                if evidencia_serializer.is_valid():
                    evidencia_serializer.save()
                else:
                    return Response(evidencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({"message": "Archivos adjuntos guardados correctamente"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)