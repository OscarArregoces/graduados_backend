from django.urls import path

from src.application.eventos.api.views.presupuesto.views import PresupuestoView

urlpatterns = [
    path("<int:actividad_id>/", PresupuestoView.as_view()),
]
