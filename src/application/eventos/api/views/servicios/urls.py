
from django.urls import path
from django.conf.urls import include
from src.application.eventos.api.views.servicios.views import ServiciosView
from src.application.eventos.api.views.subAreas.views import SubAreaViewSet

urlpatterns = [
    path("", ServiciosView.as_view()),
]
