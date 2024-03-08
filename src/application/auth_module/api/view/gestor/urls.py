from django.urls import path
from src.application.auth_module.api.view.gestor.view import GestorView

urlpatterns = [
    path("", GestorView.as_view()),
]
