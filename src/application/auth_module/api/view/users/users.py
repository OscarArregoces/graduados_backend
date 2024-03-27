from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.generics import UpdateAPIView
from rest_framework import status
from configs.helpers.PaginationView import DecoratorPaginateView
from configs.helpers.formatDate import formatDate
from configs.helpers.excelTools import formateCondicionVulnerable, formateDepartamento, formateDocumentType, formateGenderType, formateMunicipio, formateNationaliy
from src.application.auth_module.api.serializers.carrera.carrera_serializers import CarreraSerializers, CarreraSimpleSerializers

from src.application.auth_module.api.serializers.person.persons_serializers import PersonsCreateSerializer, PersonsDetailSerializers, PersonsSimpleSerializersView, UserEventoSerializer
from src.application.auth_module.api.serializers.roles.roles_serializers import RolesSerializers
from ...serializers.user.users_serializers import (
    UserSerializers,
    CreateUserSerializers,
    UserChangePassword,
)
from ....models import Carrera, Persons, User
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from typing import Optional
from src.factory.auth_interactor import AuthViewSetFactory
import pandas as pd

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.db import transaction
from datetime import datetime


CACHE_TTL = getattr(settings, "CACHE_TTL", DEFAULT_TIMEOUT)


# @method_decorator(cache_page(CACHE_TTL), name="dispatch")
class UserViewSet(ViewSet):
    viewset_factory: AuthViewSetFactory = None
    http_method_names: Optional[list[str]] = []
    model = None

    def get_serializer_class(self):
        if self.action in ["get", "get_all"]:
            return UserSerializers
        return CreateUserSerializers

    @property
    def controller(self):
        return self.viewset_factory.create(self.model, self.get_serializer_class())

    def get(self, request, *args, **kwargs):
        payload, status = self.controller.get_users(False)
        return Response(data=payload, status=status)

    def post(self, request, *args, **kwargs):
        payload, status = self.controller.post(request.data)
        return Response(data=payload, status=status)

    def put(self, request, *args, **kwargs):
        instance_id = kwargs.get("id", "")
        payload, status = self.controller.put(int(instance_id), request.data)
        return Response(data=payload, status=status)

    def delete(self, request, *args, **kwargs):
        instance_id = kwargs.get("id", "")

        if "ids" in request.data:
            payload, status = self.controller.delete(
                None, request.data.get("ids", None)
            )
            return Response(data=payload, status=status)

        payload, status = self.controller.delete(int(instance_id), request.data)
        return Response(data=payload, status=status)

    def get_users(self, request, *args, **kwargs):
        payload, status = self.controller.get_users()
        return Response(data=payload, status=status)


class UserChangePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def get_object(self):
        try:
            request_user = self.kwargs["pk"]
            user = User.objects.get(pk=request_user)
            return user
        except (User.DoesNotExist, TypeError):
            return None
        except (BaseException, TypeError) as e:
            return None

    def perform_update(self, serializer):
        if "original_password" in self.request.data:  # type: ignore
            password = make_password(self.request.data["password"])  # type: ignore
            serializer.save(password=password)
        else:
            serializer.save()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        user = request.user

        if user is None:
            return Response("User don't exist", status.HTTP_400_BAD_REQUEST)  # type: ignore

        if "original_password" not in self.request.data:  # type: ignore
            return Response("Password Error", status.HTTP_400_BAD_REQUEST)

        if not user.check_password(request.data["original_password"]):
            return Response("Password is not correct.", status.HTTP_400_BAD_REQUEST)

        user_serializers = UserChangePassword(user, data=request.data, partial=partial)

        try:
            if user_serializers.is_valid():
                self.perform_update(user_serializers)
                return Response("Password Change", status.HTTP_200_OK)
            return Response(user_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except (AttributeError, Exception) as e:
            return Response(e.args, status.HTTP_400_BAD_REQUEST)
         
# class GraduadosView(APIView):
#     @DecoratorPaginateView
#     def get(self, request, *args, **kwargs):
#         try:
#             personas = Persons.objects.filter(graduado=True).exclude(id__in=[1, 2]).all()
#             serializer = PersonsSimpleSerializersView(personas, many=True)
#             return serializer.data
#         except Exception as e :
#            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GraduadosView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            graduado_id = kwargs.get("graduado_id",None)
            print(kwargs)
            if graduado_id: 
                graduado = Persons.objects.filter(graduado=True,identification=graduado_id).exclude(id__in=[1, 2])
                serializer = PersonsSimpleSerializersView(graduado, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else :
                personas = Persons.objects.filter(graduado=True).exclude(id__in=[1, 2]).all()
                personas_con_carreras = []

                for persona in personas:
                    carreras = Carrera.objects.filter(person=persona)  
                    persona_data = PersonsSimpleSerializersView(persona).data
                    carreras_data = []
                    for carrera in carreras:
                        serializer_carrera = CarreraSimpleSerializers(carrera)
                        carreras_data.append(serializer_carrera.data)
                           
                    persona_data['carreras'] = carreras_data
                    personas_con_carreras.append(persona_data)

                return Response(personas_con_carreras, status=status.HTTP_200_OK)
        except Exception as e :
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class GraduadoDetailView(APIView):
    def get(self, request, graduado_id, *args, **kwargs):
        graduado = get_object_or_404(Persons, identification=graduado_id)

        if graduado is None:
            return Response("Graduado not found", status=404)
        
        carreras = Carrera.objects.filter(person=graduado)
        carrera_serializer = CarreraSerializers(carreras, many=True)
        persona_serializer = PersonsDetailSerializers(graduado)
        
        return Response({
            "persona": persona_serializer.data,
            "carreras": carrera_serializer.data
            }, status=status.HTTP_200_OK)

class FuncionariosView(APIView):
    @DecoratorPaginateView
    def get(self, request, *args, **kwargs):
        try:
            funcionario_id = kwargs.get("funcionario_id",None)
            if funcionario_id:
                funcionarios = Persons.objects.filter(funcionario=True,identification=funcionario_id).exclude(id__in=[1, 2])
                serializer = PersonsSimpleSerializersView(funcionarios, many=True)
                return serializer.data
            else :
                funcionarios = Persons.objects.filter(funcionario=True).exclude(id__in=[1, 2])
                serializer = PersonsSimpleSerializersView(funcionarios, many=True)
                return serializer.data
        except Exception as e :
           return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
    @transaction.atomic       
    def post(self, request, *args, **kwargs):
        persons_serializer = PersonsCreateSerializer(data=request.data)
        if persons_serializer.is_valid():
            persona = persons_serializer.save()
            # persona = persons_serializer.save(userId = request.user.id)
            identification = request.data['identification']
            usuario_data = {
                'username': str(identification),
                'password': make_password(str(identification)),
                'person_id': persona.id,
            }
            usuario_serializer = CreateUserSerializers(data=usuario_data)
            if usuario_serializer.is_valid():
                usuario_serializer.save()
                return Response({'message': 'Funcionario creado correctamente'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': persons_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class FuncionarioRolesView(APIView):
    def get(self, request, funcionario_id, *args, **kwargs):
        funcionario = Persons.objects.filter(
            identification=funcionario_id,
            funcionario=True
        ).exclude(id__in=[1, 2]).first()
        
        serializer = PersonsSimpleSerializersView(funcionario)
        usuario = User.objects.filter(person=funcionario).first()
        if usuario:
            groups = Group.objects.filter(user=usuario).all()
            roles_serializer = RolesSerializers(groups, many=True)
            
            response_data = {
                'persona': serializer.data,
                'roles': roles_serializer.data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            # Manejar el caso en el que el usuario no existe
            return Response({'error': 'El usuario asociado al funcionario no existe.'}, status=status.HTTP_404_NOT_FOUND)
        
class UserEventoView(APIView):
    # @DecoratorPaginateView
    def get(self, request, *args, **kwargs):
        persona_id = kwargs.get("persona_id",None)
        if persona_id is None:
            return Response({"error": "persona_id es requerido"}, status=status.HTTP_404_NOT_FOUND)
        try:
            persona = Persons.objects.filter(identification=persona_id).exclude(id__in=[1, 2])
            if not persona.exists():
                return Response({"error": "Persona no encontrada"}, status=status.HTTP_404_NOT_FOUND)
            
            # usuario = persona.user_set.first()

                
            serializer = UserEventoSerializer(persona, many=True)
            return Response({"user": persona[0].user_set.all().first().id , "persona": serializer.data[0]}, status=status.HTTP_200_OK)
 
        except Exception as e :
           return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       

class CargarUsuariosExcel(APIView):
    @transaction.atomic       
    def post(self, request, *args, **kwargs):
        archivo_excel = request.FILES.get('archivo_excel')
        if archivo_excel:
            try:
                df = pd.read_excel(archivo_excel)

                for index, row in df.iterrows():
                    try:
                        person_instancia = Persons.objects.get(identification=row['NUM_DOCUMENTO'])
                        carrera_data = {
                            'programa': row['PROGRAMA DE GRADO'] if pd.notna(row['PROGRAMA DE GRADO']) else "",
                            'fecha_grado': formatDate(row['FECHA DE GRADO']),
                            'modalidad_grado':  row['MODALIDAD_GRADO'] if pd.notna(row['MODALIDAD_GRADO']) else "",
                            'proyecto_grado': row['PROYECTO DE GRADO'] if pd.notna(row['PROYECTO DE GRADO']) else "",
                            'periodo_grado': row['PERIODO DE GRADO'] if pd.notna(row['PERIODO DE GRADO']) else "",
                            'numero_acta': row['NUMERO DE ACTA'] if pd.notna(row['NUMERO DE ACTA']) else "",
                            'numero_folio': row['NUMERO DE FOLIO'] if pd.notna(row['NUMERO DE FOLIO']) else "",
                            'sede': row['SEDE'] if pd.notna(row['SEDE']) else "",
                            'direccion_intitucional': row['DIRECCION_INSTITUCIONAL'] if pd.notna(row['DIRECCION_INSTITUCIONAL']) else "",
                            'person_id': person_instancia.pk
                        }
                        
                        Carrera.objects.create(**carrera_data)
                        
                    except Persons.DoesNotExist:

                        gender_type = formateGenderType(row['GENERO'])
                        document_type = formateDocumentType(row['TIPO_IDENTIFICACION'])
                        condicion_vulnerable = formateCondicionVulnerable(row['CONDICION VULNERABLE'])
                        nationality = formateNationaliy(row['PAIS DE NACIMIENTO'])
                        departamento = formateDepartamento(row['CIUDAD(DPTO)'])
                        ciudad = formateMunicipio(row['CIUDAD(DPTO)'])

                        person_data = {
                            'fullname': row['NOMBRE'] if pd.notna(row['NOMBRE']) else "",
                            'identification': row['NUM_DOCUMENTO'] if pd.notna(row['NUM_DOCUMENTO']) else "",
                            'address': row['DIRECCION'] if pd.notna(row['DIRECCION']) else "",
                            'nationality_id': nationality,
                            'departamento_id': departamento,
                            'municipio_id': ciudad,
                            'phone': row['CELULAR'] if pd.notna(row['CELULAR']) else "",
                            'phone2': row['CELULAR 2'] if pd.notna(row['CELULAR 2']) else "",
                            'fecha_expedicion': formatDate(row['FECHA_EXPEDICION']), 
                            'date_of_birth': formatDate(row['FECHA_NACIMIENTO']), 
                            'condicion_vulnerable_id': condicion_vulnerable,
                            'email': row['CORREO'] if pd.notna(row['CORREO']) else "",
                            'email2': row['CORREO 2'] if pd.notna(row['CORREO 2']) else "",
                            'document_type_id': document_type,
                            'gender_type_id': gender_type,
                        }
                        
                        persons_instance = Persons.objects.create(**person_data)
                        
                        user_data = {
                            'username': str(row['NUM_DOCUMENTO']),
                            'password': make_password(str(row['NUM_DOCUMENTO'])),
                            'person_id': persons_instance.pk,
                        }
                        
                        user_instance= User.objects.create(**user_data)
                        
                        rol_especifico, creado = Group.objects.get_or_create(name='Graduado')
                        user_instance.groups.add(rol_especifico)
                        user_instance.save()
                                                
                        carrera_data = {
                            'programa': row['PROGRAMA DE GRADO'],
                            'fecha_grado': formatDate(row['FECHA DE GRADO']),
                            'modalidad_grado':  row['MODALIDAD_GRADO'] if pd.notna(row['MODALIDAD_GRADO']) else "",
                            'proyecto_grado': row['PROYECTO DE GRADO'] if pd.notna(row['PROYECTO DE GRADO']) else "",
                            'periodo_grado': row['PERIODO DE GRADO'] if pd.notna(row['PERIODO DE GRADO']) else "",
                            'numero_acta': row['NUMERO DE ACTA'] if pd.notna(row['NUMERO DE ACTA']) else "",
                            'numero_folio': row['NUMERO DE FOLIO'] if pd.notna(row['NUMERO DE FOLIO']) else "",
                            'sede': row['SEDE'] if pd.notna(row['SEDE']) else "",
                            'direccion_intitucional': row['DIRECCION_INSTITUCIONAL'] if pd.notna(row['DIRECCION_INSTITUCIONAL']) else "",
                            'person_id': persons_instance.pk
                        }
                        
                        Carrera.objects.create(**carrera_data)
                        
                return Response({'message': 'Usuarios cargados correctamente'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': f'Error al procesar el archivo: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No se proporcionó un archivo Excel'}, status=status.HTTP_400_BAD_REQUEST)
        

    
class GenerarJsonByExcel(APIView):
    @transaction.atomic       
    def post(self, request, *args, **kwargs):
        archivo_excel = request.FILES.get('archivo_excel')
        if archivo_excel:
            try:
                df = pd.read_excel(archivo_excel)
                personas_con_carreras = []
                
                for index, row in df.iterrows():
                    persona_existente = False
                    
                    for persona in personas_con_carreras:
                        if persona['persona']["identification"] == row['NUM_DOCUMENTO']:
                            carrera_data = {
                                'programa': row['PROGRAMA DE GRADO'] if pd.notna(row['PROGRAMA DE GRADO']) else "",
                                # 'fecha_grado': row['FECHA DE GRADO'].strftime('%Y-%m-%d') if pd.notna(row['FECHA DE GRADO']) else "",
                                'modalidad_grado':  row['MODALIDAD_GRADO'] if pd.notna(row['MODALIDAD_GRADO']) else "",
                                'proyecto_grado': row['PROYECTO DE GRADO'] if pd.notna(row['PROYECTO DE GRADO']) else "",
                                'periodo_grado': row['PERIODO DE GRADO'] if pd.notna(row['PERIODO DE GRADO']) else "",
                                'numero_acta': row['NUMERO DE ACTA'] if pd.notna(row['NUMERO DE ACTA']) else "",
                                'numero_folio': row['NUMERO DE FOLIO'] if pd.notna(row['NUMERO DE FOLIO']) else "",
                                'sede': row['SEDE'] if pd.notna(row['SEDE']) else "",
                                'direccion_intitucional': row['DIRECCION_INSTITUCIONAL'] if pd.notna(row['DIRECCION_INSTITUCIONAL']) else "",
                            }
                            persona['carreras'].append(carrera_data)
                            persona_existente = True
                            break
                    
                    if not persona_existente:
                        payload = {
                            "user":{},
                            "persona": {
                                "identification": row['NUM_DOCUMENTO']
                            },
                            "carreras": []
                        }
                        gender_type = formateGenderType(row['GENERO'])
                        document_type = formateDocumentType(row['TIPO_IDENTIFICACION'])
                        condicion_vulnerable = formateCondicionVulnerable(row['CONDICION VULNERABLE'])
                        nationality = formateNationaliy(row['PAIS DE NACIMIENTO'])
                        departamento = formateDepartamento(row['CIUDAD(DPTO)'])
                        ciudad = formateMunicipio(row['CIUDAD(DPTO)'])
                        
                        person_data = {
                            'fullname': row['NOMBRE'] if pd.notna(row['NOMBRE']) else "",
                            'address': row['DIRECCION'] if pd.notna(row['DIRECCION']) else "",
                            'nationality_id': nationality,
                            'departamento_id': departamento,
                            'municipio_id': ciudad,
                            'phone': row['CELULAR'] if pd.notna(row['CELULAR']) else "",
                            'phone2': row['CELULAR 2'] if pd.notna(row['CELULAR 2']) else "",
                            # 'fecha_expedicion': row['FECHA_EXPEDICION'].strftime('%Y-%m-%d') if pd.notna(row['FECHA_EXPEDICION']) else "", 
                            # 'date_of_birth': row['FECHA_NACIMIENTO'].strftime('%Y-%m-%d') if pd.notna(row['FECHA_NACIMIENTO']) else "", 
                            'condicion_vulnerable_id': condicion_vulnerable,
                            'email': row['CORREO'] if pd.notna(row['CORREO']) else "",
                            'email2': row['CORREO 2'] if pd.notna(row['CORREO 2']) else "",
                            'document_type_id': document_type,
                            'gender_type_id': gender_type,
                        }
                        payload['persona'].update(person_data)
                        
                        user_data = {
                            'username': str(row['NUM_DOCUMENTO']),
                            'password': str(row['NUM_DOCUMENTO']),
                        }
                        
                        payload['user'] = user_data
                        
                        carrera_data = {
                            'programa': row['PROGRAMA DE GRADO'],
                            # 'fecha_grado': row['FECHA DE GRADO'].strftime('%Y-%m-%d') if pd.notna(row['FECHA DE GRADO']) else "",
                            'modalidad_grado':  row['MODALIDAD_GRADO'] if pd.notna(row['MODALIDAD_GRADO']) else "",
                            'proyecto_grado': row['PROYECTO DE GRADO'] if pd.notna(row['PROYECTO DE GRADO']) else "",
                            'periodo_grado': row['PERIODO DE GRADO'] if pd.notna(row['PERIODO DE GRADO']) else "",
                            'numero_acta': row['NUMERO DE ACTA'] if pd.notna(row['NUMERO DE ACTA']) else "",
                            'numero_folio': row['NUMERO DE FOLIO'] if pd.notna(row['NUMERO DE FOLIO']) else "",
                            'sede': row['SEDE'] if pd.notna(row['SEDE']) else "",
                            'direccion_intitucional': row['DIRECCION_INSTITUCIONAL'] if pd.notna(row['DIRECCION_INSTITUCIONAL']) else "",
                        }
                        payload['carreras'].append(carrera_data)
                        personas_con_carreras.append(payload)
                

                return Response({'graduados':  personas_con_carreras}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': f'Error al procesar el archivo: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No se proporcionó un archivo Excel'}, status=status.HTTP_400_BAD_REQUEST)
