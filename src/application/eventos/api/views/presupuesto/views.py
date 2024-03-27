from rest_framework.views import APIView   
from rest_framework.response import Response
from rest_framework import status

from src.application.eventos.api.serializers.eventos.Presupuesto_serializers import BienEquipoCreateSerializer, MaterialSuministroCreateSerializer, PersonalCreateSerializer, PresupuestoCreateSerializer, PresupuestoPayloadValidateSerializer, PresupuestoSerializer, TipoPresupuestoSerializer
from src.application.eventos.models.models import BienEquipo, Eventos, MaterialSuministro, Personal, Presupuesto

class PresupuestoView(APIView):
    def get (self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id',None)
        
        if actividad_id is None:
            return Response({"error":"actividad_id es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            actividad = Eventos.objects.filter(id=actividad_id).first()
            
            if actividad is None:
                return Response({"error": "La actividad no existe"}, status=status.HTTP_404_NOT_FOUND)
            
            presupuesto = Presupuesto.objects.filter(actividad=actividad_id).first()
            bienesEquipo = BienEquipo.objects.filter(presupuesto=presupuesto)
            materialSuministro = MaterialSuministro.objects.filter(presupuesto=presupuesto)
            personal = Personal.objects.filter(presupuesto=presupuesto)
            
            if presupuesto is None:
                return Response({"actividad": actividad.nombre_actividad, "presupuesto": None, "mostrar_formulario": True}, status=200)
        
            presupuesto_serializer = PresupuestoSerializer(presupuesto)
            bienesEquipo = TipoPresupuestoSerializer(bienesEquipo, many=True)
            materialSuministro = TipoPresupuestoSerializer(materialSuministro, many=True)
            personal = TipoPresupuestoSerializer(personal, many=True)
            
            presupuesto_response ={
                "actividad": actividad.nombre_actividad,
                "presupuesto": {
                    "total_presupuesto": presupuesto_serializer.data['total_presupuesto'],
                    "bienesEquipo": bienesEquipo.data,
                    "materialSuministro": materialSuministro.data,
                    "personal": personal.data,
                },
                "mostrar_formulario": False
                }
            
            return Response(presupuesto_response, status=200)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        actividad_id = kwargs.get('actividad_id',None)
        
        if actividad_id is None:
            return Response({"error":"actividad_id es requerido"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = PresupuestoPayloadValidateSerializer().validate(request.data)
        try:
            actividad = Eventos.objects.filter(id=actividad_id).first()
            
            if actividad is None:
                return Response({"error": "La actividad no existe"}, status=status.HTTP_404_NOT_FOUND)
            
            presupuesto_exist = Presupuesto.objects.filter(actividad=actividad_id).first()
                        
            if not presupuesto_exist is None:
                return Response({"error": "Ya existe un presupuesto para esta actividad"}, status=status.HTTP_400_BAD_REQUEST )
            
            presupuesto_serializer = PresupuestoCreateSerializer(data={'actividad': actividad.id ,'total_presupuesto':data['totalPresupuesto']})
                
            if not presupuesto_serializer.is_valid():
                return Response(presupuesto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            presupuestoCreated = presupuesto_serializer.save()
            
            for bien_equipo_data in data.get('bienesEquipos', []):
                bien_equipo_data['presupuesto'] = presupuestoCreated.id
                bien_equipo_serializer = BienEquipoCreateSerializer(data=bien_equipo_data)
                if bien_equipo_serializer.is_valid():
                    bien_equipo_serializer.save()
                else:
                    return Response(bien_equipo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
            for material_data in data.get('materialesSuministros', []):
                material_data['presupuesto'] = presupuestoCreated.id
                material_serializer = MaterialSuministroCreateSerializer(data=material_data)
                if material_serializer.is_valid():
                    material_serializer.save()
                else:
                    return Response(material_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            for personal_data in data.get('personal', []):
                personal_data['presupuesto'] = presupuestoCreated.id
                personal_serializer = PersonalCreateSerializer(data=personal_data)
                if personal_serializer.is_valid():
                    personal_serializer.save()
                else:
                    return Response(personal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Presupuesto y elementos creados exitosamente"}, status=status.HTTP_200_OK)    
            
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

                    # bienesEquipo_serializer = BienEquipoCreateSerializer(data={data_bienes_equipo, 'presupuesto': presupuesto_serializer})
                    # materialSuministro_serializer = MaterialSuministroCreateSerializer(data={})
                    # personal_serializer = PersonalCreateSerializer(data={})