from attr import fields
from django.forms import BooleanField
from ....models import Document_types, Genders, Persons
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    EmailField,
    DateField,
    IntegerField,
    PrimaryKeyRelatedField,
)
from ..document.document_serializers import DocumentSerializersView
from ..gender.gender_Serializers import GenderSerializersView
from ..user.users_serializers import UserSerializersSimple
from rest_framework.validators import UniqueValidator


class PersonsSerializers(Serializer):
    document_type = DocumentSerializersView(required=False)
    gender_type = GenderSerializersView(required=False)
    address = CharField(required=False)
    nationality = CharField(required=False)
    date_of_birth = CharField(required=False)
    phone2 = CharField(required=False)
    email2 = CharField(required=False, allow_blank=True)
    document_type = IntegerField(required=False)
    gender_type = IntegerField(required=False)
    # user = UserSerializersSimple(read_only=True, expands=False)

    class Meta:
        model = Persons
        exclude = ("createdAt", "updateAt", "visible", "userCreate", "userUpdate", "status","name")
    
    def create(self, validated_data,):
        # validated_data.get('userId',None)
        document_type_id = validated_data.pop('document_type', None)
        gender_type_id = validated_data.pop('gender_type', None)

        if document_type_id:
            validated_data['document_type'] = Document_types.objects.get(pk=document_type_id)

        if gender_type_id:
            validated_data['gender_type'] = Genders.objects.get(pk=gender_type_id)
            
        
        return Persons.objects.create(**{**validated_data, 'email2':None,})
    
    # def create(self, validated_data):
    #     return Persons.objects.create(**validated_data)


class PersonsCreateSerializer(ModelSerializer):
    class Meta:
        model = Persons
        fields = '__all__'

class PersonsDetailSerializers(ModelSerializer):
     class Meta:
        model = Persons
        exclude = ("createdAt", "updateAt", "visible", "userCreate", "userUpdate", "status","name")
    
class PersonsSimpleSerializersView(ModelSerializer):

    gender_type = GenderSerializersView(read_only=True)
    
    class Meta:
        model = Persons
        fields = ('id','fullname','email','nationality','identification','gender_type')



queryset = Persons.objects.all()

class PersonsSerializer(Serializer):
    name = CharField(write_only=True, validators=[UniqueValidator(queryset=queryset)])
    surname = CharField(write_only=True, required=False)
    identification = CharField(
        write_only=True, required=False, validators=[UniqueValidator(queryset=queryset)]
    )
    address = CharField(write_only=True, required=False)
    nationality = CharField(write_only=True, required=False)
    date_of_birth = DateField(write_only=True, required=False)
    phone = CharField(write_only=True, required=False)


class UsuariosExcelSerializersView(Serializer):
    name = CharField()
    nationality = CharField()
    municipio = CharField()
    departamento = CharField()
    address = CharField()
    condicion_vulnerable = CharField()
    estado_civil = CharField()
    phone = CharField()
    phone2 = CharField()
    email = CharField()
    email2 = CharField()
    programa = CharField()
    sede = CharField()
    modalidad_grado = CharField()
    proyecto_grado = CharField()
    periodo_grado = CharField()
    numero_acta = CharField()
    numero_folio = CharField()
    saber_pro = CharField()
    direccion_intitucional = CharField()
    identification = CharField()
    document_type = CharField()
    genero = CharField()
  
# class FuncionarioSerializers(Serializer):
#     fullname  = CharField()
#     identification  = CharField()
#     address  = CharField()
#     nationality  = CharField()
#     date_of_birth  = DateField()
#     phone  = CharField()
#     phone2  = CharField()
#     fecha_expedicion  = DateField()
#     condicion_vulnerable  = CharField()
#     municipio  = CharField()
#     departamento  = CharField()
#     email  = CharField()
#     email2  = CharField()
#     graduado  = BooleanField()
#     funcionario  = BooleanField()
#     document_type = IntegerField()
#     gender_type = IntegerField()
  