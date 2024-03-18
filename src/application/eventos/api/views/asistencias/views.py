from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework import status
from src.application.auth_module.models import User
from src.application.eventos.api.serializers.eventos.Asistencias_serializers import AsistenciaCreateSerializer, AsistenciaExternoCreateSerializer, AsistenciaReporteExternosSerializer, AsistenciarReporteSerializer
from src.application.eventos.models.models import Asistencia, AsistenciaExternos, Eventos
from django.db import transaction
from django.db.models import Count
from collections import defaultdict

class AsistenciasView(APIView):
    def get(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id', None)
        if actividad_id is None:
            return Response({"error":"actividad_id es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            asistencias = Asistencia.objects.filter(actividad=actividad_id)
            asistencias_externos = AsistenciaExternos.objects.filter(actividad=actividad_id)
            
            asistencias_serializer = AsistenciarReporteSerializer(asistencias, many=True)
            asistencias_externos_serializer = AsistenciaReporteExternosSerializer(asistencias_externos, many=True)
            
            # IMPACTO
            
            confirmacion_asistencia = defaultdict(int)
            asistencia_real = defaultdict(int)

            # Iterar sobre las asistencias
            for asistencia in asistencias:
                # Contar confirmaciones de asistencia
                if asistencia.confirmacion:
                    confirmacion_asistencia['confirmaron'] += 1
                else:
                    confirmacion_asistencia['no_confirmaron'] += 1
                
                # Contar asistencias reales
                if asistencia.asistencia:
                    asistencia_real['asistieron'] += 1
                else:
                    asistencia_real['no_asistieron'] += 1

            # CONTEO
            
            conteo_externos = asistencias_externos.values('vinculacion').annotate(conteo=Count('vinculacion'))
            resultados_externos = {}
            
            for item in conteo_externos:
                vinculacion = item['vinculacion']
                conteo = item['conteo']
                resultados_externos[vinculacion] = conteo
            
            resultados_asistencias_graduados = 0
            resultados_asistencias_funcionarios = 0
            
            for persona in asistencias_serializer.data:
                if persona['asistencia'] and persona['graduado']:
                    resultados_asistencias_graduados += 1
                elif persona['asistencia'] and persona['funcionario']:
                    resultados_asistencias_funcionarios += 1

            asistencias_list = [
                {"name": "graduados", "cantidad": resultados_asistencias_graduados},
                {"name": "funcionarios", "cantidad": resultados_asistencias_funcionarios},
            ]

            # Agregar los datos de asistencias externas al resultado
            for vinculacion, conteo in resultados_externos.items():
                asistencias_list.append({"name": vinculacion, "cantidad": conteo})
            
            return Response({
                "conteo": asistencias_list,
                "impactos": [
                    {"name": "Confirmación Asistencia", "si": confirmacion_asistencia['confirmaron'] , "no": confirmacion_asistencia['no_confirmaron']},
                    {"name": "Asistencia", "si": asistencia_real['asistieron'] , "no": asistencia_real['no_asistieron']},
                    
                    # {"name": "Confirmaron asistencia", "value": confirmacion_asistencia['confirmaron']},
                    # {"name": "No confirmaron asistencia", "value": confirmacion_asistencia['no_confirmaron']},
                    # {"name": "Asistieron", "value": asistencia_real['asistieron']},
                    # {"name": "No asistieron", "value": asistencia_real['no_asistieron']},
                ],
                "asistencia": asistencias_serializer.data, 
                "asistencia_externos": asistencias_externos_serializer.data
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id', None)
        if actividad_id is None:
            return Response({"error":"actividad_id es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        user_id = request.data.get('user')
        if user_id is None:
            return Response({"error":"user es requerido"}, status=status.HTTP_400_BAD_REQUEST)
            
        try:
            isExist = Asistencia.objects.filter(actividad=actividad_id, user=user_id).first()
            actividad = Eventos.objects.filter(id=actividad_id).first()
            
            if actividad is None:
                return Response({"error":"Actividad no existe"}, status=status.HTTP_404_NOT_FOUND)
            
            if actividad.fecha_inicio > timezone.now():
                return Response({"error": "Esta actividad aún no ha iniciado"}, status=status.HTTP_400_BAD_REQUEST)
            
            if actividad.fecha_final < timezone.now():
                return Response({"error": "Esta actividad ya ha finalizado"}, status=status.HTTP_400_BAD_REQUEST)
            
            if not isExist is None:
                if isExist.asistencia :
                    return Response({"error":"Usted ya esta inscrito a esta actividad"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    isExist.asistencia = True
                    isExist.save()
                    return Response({"success": "Asistencia registrada"}, status=status.HTTP_200_OK)
            payload = {
                "actividad": request.data.get('actividad'),
                "user": request.data.get('user'),
                "asistencia": True
                }
            asistencia_serializer = AsistenciaCreateSerializer(data=payload)
            if asistencia_serializer.is_valid():
                asistencia_serializer.save()
            else:
                return Response(asistencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
            try:
                user = User.objects.select_related('person').get(id=user_id)
                body = {}
                body['persona'] =  user.person.fullname
                body['actividad'] = actividad.nombre_actividad
                body['message'] = "Asistencia registrada"
                return Response(body, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error":"Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)
                
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
class AsistenciasExternosView(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            actividad_id = request.data.get('actividad', None)
            document = request.data.get('document', None)
            isExist = AsistenciaExternos.objects.filter(actividad=actividad_id, document=document).first()
            actividad = Eventos.objects.filter(id=actividad_id).first()
            
            if actividad is None:
                return Response({"error":"Actividad no existe"}, status=status.HTTP_404_NOT_FOUND)
            
            if actividad.fecha_inicio > timezone.now():
                return Response({"error": "Esta actividad aún no ha iniciado"}, status=status.HTTP_400_BAD_REQUEST)
            
            if actividad.fecha_final < timezone.now():
                return Response({"error": "Esta actividad ya ha finalizado"}, status=status.HTTP_400_BAD_REQUEST)
            
            if not isExist is None:
                return Response({"error":"Usted ya esta inscrito a esta actividad"}, status=status.HTTP_400_BAD_REQUEST)
            
            asistencia_serializer = AsistenciaExternoCreateSerializer(data=request.data)
            
            if asistencia_serializer.is_valid():
                asistencia_serializer.save()
            else:
                return Response(asistencia_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            body = {}
            body['persona'] = asistencia_serializer.data['fullname']
            body['actividad'] = actividad.nombre_actividad
            return Response(body, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
        
class AsistenciasDetalleView(APIView):
    def get(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id', None)
        if actividad_id is None:
            return Response({"error":"actividad_id es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            asistencias = Asistencia.objects.filter(actividad=actividad_id)
            asistencias_externos = AsistenciaExternos.objects.filter(actividad=actividad_id)
            
            asistencias_serializer = AsistenciarReporteSerializer(asistencias, many=True)
            asistencias_externos_serializer = AsistenciaReporteExternosSerializer(asistencias_externos, many=True)

            # CONTEO
            
            conteo_externos = asistencias_externos.values('vinculacion').annotate(conteo=Count('vinculacion'))
            resultados_externos = {}
            
            for item in conteo_externos:
                vinculacion = item['vinculacion']
                conteo = item['conteo']
                resultados_externos[vinculacion] = conteo
            
            resultados_asistencias_graduados = 0
            resultados_asistencias_funcionarios = 0
            
            for persona in asistencias_serializer.data:
                if persona['asistencia'] and persona['graduado']:
                    resultados_asistencias_graduados += 1
                elif persona['asistencia'] and persona['funcionario']:
                    resultados_asistencias_funcionarios += 1

            asistencias_list = [
                {"name": "Graduados", "cantidad": resultados_asistencias_graduados},
                {"name": "Funcionarios", "cantidad": resultados_asistencias_funcionarios},
            ]

            # Agregar los datos de asistencias externas al resultado
            for vinculacion, conteo in resultados_externos.items():
                asistencias_list.append({"name": vinculacion, "cantidad": conteo})
            
            return Response({
                "conteo": asistencias_list,
                "asistencia": asistencias_serializer.data, 
                "asistencia_externos": asistencias_externos_serializer.data
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)