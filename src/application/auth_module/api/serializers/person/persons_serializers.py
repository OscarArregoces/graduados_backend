from attr import fields
from ....models import Persons
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    DateField,
    IntegerField,
    PrimaryKeyRelatedField,
)
from ..document.document_serializers import DocumentSerializersView
from ..gender.gender_Serializers import GenderSerializersView
from ..user.users_serializers import UserSerializersSimple
from rest_framework.validators import UniqueValidator


class PersonsSerializers(ModelSerializer):
    document_type = DocumentSerializersView(read_only=True)
    gender_type = GenderSerializersView(read_only=True)
    identification = CharField( required=False)
    email = CharField( required=False)
    # user = UserSerializersSimple(read_only=True, expands=False)

    class Meta:
        model = Persons
        exclude = ("createdAt", "updateAt", "visible", "userCreate", "userUpdate", "status","name")


class PersonsSimpleSerializersView(ModelSerializer):

    gender_type = GenderSerializersView(read_only=True)
    
    class Meta:
        model = Persons
        fields = ('id','fullname','email','nationality','identification','gender_type')


class PersonsSimpleSerializers(Serializer):
    name = CharField()
    document_type = IntegerField()
    surname = CharField()
    identification = IntegerField()
    address = CharField()
    nationality = CharField()
    date_of_birth = DateField()
    gender_type = CharField()
    phone = CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        person = Persons.objects.create(
            name=validated_data["name"],
            document_type_id=validated_data["document_type"],
            surname=validated_data["surname"],
            identification=validated_data["identification"],
            address=validated_data["address"],
            nationality=validated_data["nationality"],
            date_of_birth=validated_data["date_of_birth"],
            gender_type_id=validated_data["gender_type"],
            phone=validated_data["phone"],
        )
        return person

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.document_type_id = validated_data.get(
            "document_type", instance.document_type
        )
        instance.surname = validated_data.get("surname", instance.surname)
        instance.identification = validated_data.get(
            "identification", instance.identification
        )
        instance.address = validated_data.get("address", instance.address)
        instance.nationality = validated_data.get("nationality", instance.nationality)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.gender_type_id = validated_data.get(
            "gender_type", instance.gender_type
        )
        instance.phone = validated_data.get("phone", instance.phone)

        instance.save()
        return instance


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
  