from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework import status
from configs.helpers.enviarCorreos import EnviarCorreos
from src.application.eventos.api.serializers.eventos.Asistencias_serializers import AsistenciaSerializer, AsistenciarReporteSerializer
from src.application.eventos.api.serializers.eventos.eventos_serialziers import EventosCreateSerializer, EventosSerializer, EventosSimpleSerializer
from django.db import transaction
from src.application.eventos.api.serializers.eventos.ponentes_serializer import PonentesExternosCreateSerializer, PonentesExternosSerializerVew, PonentesVinculacionCreateSerializer, PonentesVinculacionSerializerView
from src.application.eventos.models.models import Asistencia, AsistenciaExternos, Eventos, EventosServicios, EventosStatus, PonentesExternos, PonentesVinculacion
from django.shortcuts import get_object_or_404
from django.utils import timezone
import json
from django.db.models import Count


class EventosView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            eventos = Eventos.objects.filter(estado_actividad_id=1)
            serializer = EventosSimpleSerializer(eventos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
    
    # @transaction.atomic 
    def post(self, request, *args, **kwargs):
        actividad_data = request.data.get('actividad', {})
        ponentes_data = request.data.get('ponentes', {})

        actividad_data['userCreate'] = request.user.id
        # Serializar la actividad
        actividad_serializer = EventosCreateSerializer(data=actividad_data)
        if not actividad_serializer.is_valid():
            return Response({'ok': False, 'message': 'Error en los datos de la actividad', 'errors': actividad_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Guardar la actividad en la base de datos
            with transaction.atomic(): 
                actividad = actividad_serializer.save()

                vinculacion_data = ponentes_data.get('vinculacion', [])

                for vinculacion_item in vinculacion_data:
                    vinculacion_serializer = PonentesVinculacionCreateSerializer(data={ 
                        "actividad": actividad.id, 
                        "user": vinculacion_item["id"], 
                        "rol": vinculacion_item["rol"], 
                        "vinculacion": vinculacion_item["vinculacion"],
                        "dedicacion": vinculacion_item["dedicacion"],
                    })
                    if vinculacion_serializer.is_valid():
                        vinculacion_serializer.save()
                    else:
                        raise Exception(vinculacion_serializer.errors)

                # Relacionar ponentes externos con la actividad
                externos_data = ponentes_data.get('externos', [])
                for externo_item in externos_data:
                    externo_item["actividad"] = actividad.id
                    externo_serializer = PonentesExternosCreateSerializer(data=externo_item)
                    if externo_serializer.is_valid():
                        externo_serializer.save()
                    else:
                        raise Exception(externo_serializer.errors)

                return Response({'ok': True, 'message': 'Actividad creada exitosamente'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            transaction.rollback()
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)
        
class EventoDetailView(APIView):
    def get(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id',None)
        if actividad_id is None:
            return Response({'errors': 'actividad_id es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            evento = Eventos.objects.filter(id=actividad_id)
            if not evento.exists():
                return Response({'errors': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

            ponentes_vinculacion = PonentesVinculacion.objects.filter(actividad=actividad_id)
            ponentes_externos = PonentesExternos.objects.filter(actividad=actividad_id)
            
            serializer_evento = EventosSerializer(evento, many=True)
            serializer_ponentes_vinculacion = PonentesVinculacionSerializerView(ponentes_vinculacion, many=True)
            serializer_ponentes_externos = PonentesExternosSerializerVew(ponentes_externos, many=True)
            
            asistencias = Asistencia.objects.filter(actividad=actividad_id)
            asistencias_externos = AsistenciaExternos.objects.filter(actividad=actividad_id)
            conteo_externos = asistencias_externos.values('vinculacion').annotate(conteo=Count('vinculacion'))

            asistencias_serializer = AsistenciarReporteSerializer(asistencias, many=True)
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
                "actividad": serializer_evento.data,
                "ponentes": {
                    "vinculacion": serializer_ponentes_vinculacion.data,
                    "externos": serializer_ponentes_externos.data,
                    },
                "asistencias":asistencias_list,
                }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


class EventosAprobacionView(APIView):
    def put(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id',None)
        body_data = json.loads(request.body)
        actividad_status = body_data.get('actividad_status', None)
        # actividad_status = request.PUT.get('actividad_status',None)
        if actividad_id is None:
            return Response({'errors': 'actividad_id es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        if actividad_status is None:
            return Response({'errors': 'actividad_status es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        
        actividad = get_object_or_404(Eventos, id=actividad_id)
        status_actividad = get_object_or_404(EventosStatus, id=actividad_status)
        actividad.estado_actividad = status_actividad
        actividad.save()

        return Response("Actividad aprobada", status=status.HTTP_200_OK)
class EventosReportesView(APIView):      
    def get(self, request, *args, **kwargs):
        try:
            fecha_actual = timezone.now()
            actividades_aprobadas = Eventos.objects.filter(
                estado_actividad_id = 2,
                fecha_final__lte = fecha_actual
            )
            estado_finalizada = EventosStatus.objects.get(id=4)

            for actividad in actividades_aprobadas:
                actividad.estado_actividad = estado_finalizada
                actividad.save()

            actividades_finalizadas = Eventos.objects.filter(estado_actividad_id=estado_finalizada)

            serializer = EventosSerializer(actividades_finalizadas, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        
class MisEventosView(APIView):    
    def get(self, request, *args, **kwargs):
        try:
            fecha_actual = timezone.now()
            actividades_aprobadas = Eventos.objects.filter(
                estado_actividad_id = 2,
                fecha_final__lte = fecha_actual
            )
            estado_finalizada = EventosStatus.objects.get(id=4)

            for actividad in actividades_aprobadas:
                actividad.estado_actividad = estado_finalizada
                actividad.save()

            actividades = Eventos.objects.filter(estado_actividad=2)
            responseData = []
            for actividad in actividades:
                currentActividad = {
                    "actividad": [],
                    "confirmacion": False,
                    "asistencia": False,
                    "ponentes": {
                        "vinculacion": [],
                        "externos": [],
                    },
                }
                asistencia = Asistencia.objects.filter(actividad=actividad, user=request.user).first()
                if asistencia is not None:
                    asistencia_serializer = AsistenciaSerializer(asistencia)
                    print(asistencia_serializer.data)
                    currentActividad['confirmacion'] = asistencia_serializer.data.get('confirmacion', False)
                    currentActividad['asistencia'] = asistencia_serializer.data.get('asistencia', False)
                    
                ponentes_vinculacion = PonentesVinculacion.objects.filter(actividad=actividad)
                ponentes_externos = PonentesExternos.objects.filter(actividad=actividad)
                
                serializer_evento = EventosSerializer([actividad], many=True)
                serializer_ponentes_vinculacion = PonentesVinculacionSerializerView(ponentes_vinculacion, many=True)
                serializer_ponentes_externos = PonentesExternosSerializerVew(ponentes_externos, many=True)
                
                currentActividad["actividad"] = serializer_evento.data        
                currentActividad["ponentes"]["vinculacion"] = serializer_ponentes_vinculacion.data        
                currentActividad["ponentes"]["externos"] = serializer_ponentes_externos.data        
                responseData.append(currentActividad)
                
            return Response(responseData, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

class InscripcionView(APIView):
    def post(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id', None)

        if actividad_id is None:
            return Response({'errors': 'actividad_id es requerido'}, status=status.HTTP_400_BAD_REQUEST)

        asistencia = Asistencia.objects.filter(actividad=actividad_id, user=request.user).first()

        if asistencia:
            # Si el registro de asistencia existe
            if asistencia.confirmacion:
                # Si la confirmación ya está en True, devuelve un error
                return Response({'errors': 'Ya confirmó su asistencia'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Actualiza el registro de asistencia para confirmar la asistencia
                asistencia.confirmacion = True
                asistencia.save()
        else:
            # Si no existe el registro de asistencia, créalo
            Asistencia.objects.create(actividad_id=actividad_id, user=request.user, confirmacion=True)

        return Response({'success': 'Asistencia confirmada'}, status=status.HTTP_200_OK)
    
class EnviarCorreo(APIView):
  def post(self, request, *args, **kwargs):
        destinatarios = ["oiarregoces@uniguajira.edu.co",]
        asunto = "¡Tu presencia es clave! 🎓 Confirma tu Asistencia"
        template = 'EventosNotificacion.html'
        # contexto = {'destinatario': 'Oscar Arregoces','destinatario': 'Ivan Riveira'}
        # EnviarCorreos(destinatarios, asunto, template, contexto)
        contextos = [
            {'destinatario': 'Oscar Arregoces', 'documento' : '1118874652'},
        ]
        
        for destinatario, contexto in zip(destinatarios, contextos):
            EnviarCorreos([destinatario], asunto, template, contexto)
        return Response({'mensaje': 'Correo enviado exitosamente'})
    