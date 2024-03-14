from django.urls import path
from django.conf.urls import include

from src.application.eventos.api.views.eventos.views import EventoDetailView, EventosAprobacionView, EventosReportesView, EventosView, InscripcionView, MisEventosView

urlpatterns = [
    path("", EventosView.as_view()),
    path("aprobacion/<int:actividad_id>/", EventosAprobacionView.as_view()),
    path("reportes/", EventosReportesView.as_view()),
    path("mis-actividades/", MisEventosView.as_view()),
    path("detalle/<int:actividad_id>/", EventoDetailView.as_view()),
    path("inscripcion/<int:actividad_id>/", InscripcionView.as_view()),
]
