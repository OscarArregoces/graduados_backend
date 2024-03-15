from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from src.application.auth_module.models import Gestor, Headquarters
from src.application.default.models import BaseModel
from django.db.models.signals import pre_save
from django.dispatch import receiver

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
    name = models.CharField(max_length=256, blank=False, null=False)
    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

class EventosServicios(BaseModel):
    actividad = models.ForeignKey('Eventos', on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)

class EventosStatus(BaseModel):
    name = models.CharField(max_length=100, blank=False, null=False)

class Eventos(BaseModel):
    id = models.IntegerField(primary_key=True, editable=False)
    nombre_actividad = models.CharField(max_length=256)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_final = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=500)
    objetivo = models.CharField(max_length=256)
    modalidad = models.CharField(max_length=100)
    enlace_reunion = models.CharField(max_length=500, blank=True, default="")
    direccion = models.CharField(max_length=256, blank=True, default="")
    tipo_actividad = models.ForeignKey(TipoEvento, on_delete=models.SET_NULL, blank=True, null=True)
    area = models.ForeignKey(EventosArea, on_delete=models.SET_NULL, blank=True, null=True)
    subarea = models.ForeignKey(SubAreaEventos, on_delete=models.SET_NULL, blank=True, null=True)
    servicios =models.ManyToManyField(Servicios,blank=True, related_name='actividades', through=EventosServicios)
    sede = models.ForeignKey(Headquarters, on_delete=models.SET_NULL, blank=True, null=True)
    dependencia = models.ForeignKey(Gestor, on_delete=models.SET_NULL, blank=True, null=True)
    estado_actividad = models.ForeignKey(EventosStatus, on_delete=models.SET_NULL, blank=True, null=True)
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        get_latest_by = "id"
        ordering = ["id"]

@receiver(pre_save, sender=Eventos)
def set_evento_id(sender, instance, **kwargs):
    if not instance.id:
        last_evento = Eventos.objects.order_by('-id').first()
        if last_evento:
            instance.id = last_evento.id + 25
        else:
            instance.id = 10525
            
class PonentesVinculacion (BaseModel):
    actividad = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=50, blank=False,default="")
    vinculacion = models.CharField(max_length=50, blank=False, default="")
    dedicacion = models.CharField(max_length=50, blank=False, default="")
    
class PonentesExternos (BaseModel):
    actividad = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    dedicacion = models.CharField(max_length=150, blank=False)
    document = models.CharField(max_length=150, blank=False)
    email = models.CharField(max_length=150, blank=False)
    fullname = models.CharField(max_length=150, blank=False)
    phone = models.CharField(max_length=150, blank=False)
    rol = models.CharField(max_length=150, blank=False)
    vinculacion = models.CharField(max_length=150, blank=False)

class Asistencia(BaseModel):
    actividad = models.ForeignKey(Eventos, on_delete=models.CASCADE, db_index=True, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+", unique=False)
    confirmacion = models.BooleanField(blank=True ,default=False)
    asistencia = models.BooleanField(blank=True ,default=False)
    
    class Meta:
        unique_together = ("actividad", "user")

class AsistenciaExternos(BaseModel):
    actividad = models.ForeignKey(Eventos, on_delete=models.CASCADE, db_index=True, unique=False)
    fullname = models.CharField(max_length=150, blank=False, default="")
    email = models.CharField(max_length=150, blank=False, default="")
    phone = models.CharField(max_length=150, blank=False, default="")
    document = models.CharField(max_length=150, blank=False, default="")
    vinculacion = models.CharField(max_length=150, blank=False, default="")
    
    class Meta:
        unique_together = ("actividad", "document")
