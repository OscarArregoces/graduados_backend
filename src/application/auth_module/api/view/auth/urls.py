from django.urls import path

from .view import AuthLoginFuncionario, AuthLoginGraduado, LogoutView

app_name = "module"

urlpatterns = [
    path("login/", AuthLoginFuncionario.as_view()),
    path("login/graduado", AuthLoginGraduado.as_view()),
    path("logout/", LogoutView.as_view()),
]
