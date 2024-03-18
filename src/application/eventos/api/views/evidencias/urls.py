from django.urls import path

from src.application.eventos.api.views.evidencias.views import EvidenciasView

urlpatterns = [
    path("<int:actividad_id>/", EvidenciasView.as_view()),
]
