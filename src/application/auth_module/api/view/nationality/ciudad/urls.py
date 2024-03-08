from django.urls import path
from src.application.auth_module.api.view.nationality.ciudad.view import CiudadesByDepartamentoView, CiudadesView

urlpatterns = [
    path("ciudad/", CiudadesView.as_view()),
    path("ciudad/byDepartamento/<int:departamento_id>/", CiudadesByDepartamentoView.as_view()),
]