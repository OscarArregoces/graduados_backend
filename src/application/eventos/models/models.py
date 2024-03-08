from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import date
from src.application.auth_module.models import Gestor, Headquarters, Programs
from configs.helpers.hour import readeable_hour
from src.application.default.models import BaseModel

User = get_user_model()


class EventosArea(BaseModel):
    def __str__(self) -> str:
        return self.name  # type: ignore

    class Meta:
        verbose_name = "Area Evento"
        verbose_name_plural = "Areas Eventos"


class SubAreaEventos(BaseModel):
    area = models.ForeignKey(
        EventosArea, on_delete=models.CASCADE, related_name="areas", db_index=True
    )

    class Meta:
        verbose_name = "Sub Area Evento"
        verbose_name_plural = "Sub Areas Eventos"


class TipoEvento(BaseModel):
    class Meta:
        verbose_name = "Tipo Evento"
        verbose_name_plural = "Tipo Eventos"
        
class Servicios(BaseModel):
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

class EventosServicios(BaseModel):
    actividad = models.ForeignKey('Eventos', on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)

class Eventos(BaseModel):
    nombre_actividad = models.CharField(max_length=256)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_final = models.DateField(blank=True, null=True)
    descripcion = models.CharField(max_length=500)
    objetivo = models.CharField(max_length=256)
    modalidad = models.CharField(max_length=100)
    enlace_reunion = models.CharField(max_length=500, blank=True, default="")
    direccion = models.CharField(max_length=256, blank=True, default="")
    tipo = models.ForeignKey(TipoEvento, on_delete=models.SET_NULL, blank=True, null=True)
    area = models.ForeignKey(EventosArea, on_delete=models.SET_NULL, blank=True, null=True)
    subArea = models.ForeignKey(SubAreaEventos, on_delete=models.SET_NULL, blank=True, null=True)
    servicios =models.ManyToManyField(Servicios,blank=True, related_name='actividades', through=EventosServicios)
    sede = models.ForeignKey(Headquarters, on_delete=models.SET_NULL, blank=True, null=True)
    dependencia = models.ForeignKey(Gestor, on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

class PonentesVinculacion (BaseModel):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class PonentesExternos (BaseModel):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    dedicacion = models.CharField(max_length=150, blank=False)
    document = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=150, blank=False)
    fullname = models.CharField(max_length=150, blank=False)
    phone = models.CharField(max_length=150, blank=False)
    rol = models.CharField(max_length=150, blank=False)
    vinculacion = models.CharField(max_length=150, blank=False)


class Inscripcion(BaseModel):
    evento = models.ForeignKey(Eventos, on_delete=models.CASCADE, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    class Meta:
        unique_together = ("evento", "user")


class Asistencia(BaseModel):
    evento = models.ForeignKey(
        Eventos, on_delete=models.CASCADE, db_index=True, unique=False
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="+", unique=False
    )
    confirm = models.BooleanField(default=False)
    asistencia = models.BooleanField(default=False)

    def clean(self):
        if self.evento.fecha < date.today():
            raise ValidationError(
                "No se puede crear la asistencia para un evento que ha pasado."
            )

    class Meta:
        unique_together = ("evento", "user")
