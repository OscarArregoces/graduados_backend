from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group
# from django.utils import timezone

from .managers.users.managers import UserManagers
from src.application.default.models import BaseModel

class Document_types(BaseModel):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Document_types"
        verbose_name_plural = "Document_types"


class Genders(BaseModel):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Genders"
        verbose_name_plural = "Genders"

class Gestor(BaseModel):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Gestor"
        verbose_name_plural = "Gestores"

class Persons(BaseModel):
    fullname = models.CharField(max_length=150, unique=False, blank=True, default="")
    identification = models.CharField(max_length=40, unique=True, blank=False, default="")
    address = models.CharField(max_length=150, blank=True, default="")
    nationality = models.CharField(max_length=100, blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, default="")
    phone2 = models.CharField(blank=True, default="",  max_length=50)
    fecha_expedicion = models.DateField(blank=True, null=True)
    condicion_vulnerable = models.CharField(blank=True, default="", max_length=300)
    municipio = models.CharField(blank=True, default="", max_length=100)
    departamento = models.CharField(blank=True, default="", max_length=100)
    email = models.EmailField(_("email address"), blank=False, default="", unique=False)
    email2 = models.EmailField(_("email address"), blank=True, default="", unique=False)
    graduado = models.BooleanField(blank=True, default=True)
    funcionario = models.BooleanField(blank=True, default=False)
    
    status = models.BooleanField(default=True)

    document_type = models.ForeignKey(
        Document_types, on_delete=models.SET_NULL, blank=True, null=True
    )
    gender_type = models.ForeignKey(
        Genders,
        related_name="gender_types",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name  # type: ignore

    class Meta:
        unique_together = ("name", "identification")
        verbose_name = "Persons"
        verbose_name_plural = "Persons"

class User(AbstractUser, BaseModel):
    username = models.CharField(blank=False, null=False, unique=True, max_length=256)
    password = models.CharField(max_length=100)
    resetToken = models.CharField(max_length=256, blank=True, null=True)
    avatar = models.CharField(max_length=256, blank=True, null=True)
    roles = models.ManyToManyField(Group, related_name="user_roles", db_index=True)
    gestor = models.ForeignKey(
        Gestor, on_delete=models.SET_NULL, blank=True, null=True
    )
    person = models.ForeignKey(
        Persons, on_delete=models.SET_NULL, blank=True, null=True, db_index=True
    )
    objects = UserManagers()

    class Meta:
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username
    
class Carrera(BaseModel):
    programa = models.CharField(blank=True, default="", max_length=300)
    fecha_grado = models.DateField(blank=True, null=True)
    modalidad_grado = models.CharField(blank=True, default="", max_length=300)
    proyecto_grado = models.CharField(blank=True, default="", max_length=500)
    periodo_grado = models.CharField(blank=True, default="", max_length=300)
    numero_acta = models.CharField(blank=True, default="", max_length=300)
    numero_folio = models.CharField(blank=True, default="", max_length=300)
    sede = models.CharField(blank=True, default="", max_length=300)
    direccion_intitucional = models.CharField(blank=True, default="", max_length=300)
    
    person = models.ForeignKey(
        Persons, on_delete=models.SET_NULL, blank=True, null=True, db_index=True
    )
    
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"


class Resources(BaseModel):
    path = models.CharField(max_length=256)
    id_padre = models.IntegerField()
    method = models.CharField(max_length=256)
    icono = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
    titulo = models.CharField(max_length=100)
    roles = models.ManyToManyField(
        Group, through="Resources_roles", related_name="resources_roles", db_index=True
    )

    class Meta:
        verbose_name = "Resources"
        verbose_name_plural = "Resources"


class Resources_roles(BaseModel):
    resourcesId = models.ForeignKey(
        Resources, on_delete=models.CASCADE, related_name="resources"
    )
    rolesId = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="resouces_roles"
    )

    def __str__(self) -> str:
        return self.resourcesId.path + "" + self.rolesId.name

    class Meta:
        verbose_name = "Resources_roles"
        verbose_name_plural = "Resources_roles"


class Headquarters(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Headquarter"
        verbose_name_plural = "Headquarters"


class Faculties(BaseModel):
    name = models.CharField(max_length=256)
    headquarter = models.ForeignKey(Headquarters, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Facultie"
        verbose_name_plural = "Faculties"


class Programs(BaseModel):
    name = models.CharField(max_length=256)
    faculty = models.ForeignKey(Faculties, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"
        
class CondicionesVulnerables(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "CondicionVulnerable"
        verbose_name_plural = "CondicionesVulnerables"
