from django.urls import path

from src.application.eventos.api.views.asistencias.views import AsistenciasDetalleView, AsistenciasExternosView, AsistenciasView

urlpatterns = [
    path("<int:actividad_id>/", AsistenciasView.as_view()),
    path("detalle/<int:actividad_id>/", AsistenciasDetalleView.as_view()),
    path("externos/", AsistenciasExternosView.as_view()),
]
