from django.urls import path, include, re_path
from src.application.constants import PATH_APP

app_name = "eventos"

urlpatterns = [
    path("", include(f"{PATH_APP}.eventos.api.views.eventos.urls")),
    path("areas/", include(f"{PATH_APP}.eventos.api.views.areas.urls")),
    path("sub/areas/", include(f"{PATH_APP}.eventos.api.views.subAreas.urls")),
    path("tipos/", include(f"{PATH_APP}.eventos.api.views.tipo_actividad.urls")),
    path("servicios/", include(f"{PATH_APP}.eventos.api.views.servicios.urls")),
    path("asistencias/", include(f"{PATH_APP}.eventos.api.views.asistencias.urls")),
    path("evidencias/", include(f"{PATH_APP}.eventos.api.views.evidencias.urls")),
    path("presupuesto/", include(f"{PATH_APP}.eventos.api.views.presupuesto.urls")),
]
