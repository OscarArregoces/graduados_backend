from src.application.auth_module.api.view.carrera.view import CarreraView
from src.application.auth_module.api.view.condiciones.view import CondicionesVulnerablesView
from ..modules import path

from django.urls import path

from src.application.auth_module.api.view.persons.persons import PersonViewSet

urlpatterns = [
    path("", CondicionesVulnerablesView.as_view()),
]

