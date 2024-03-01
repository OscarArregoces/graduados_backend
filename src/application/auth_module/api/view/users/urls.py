from django.urls import path, re_path
from .users import CargarUsuariosExcel, FuncionarioView, FuncionariosView, GraduadoDetailView, GraduadoView, GraduadosView, UserChangePasswordView

from django.conf.urls import include


from src.application.auth_module.api.view.users.route import Router
from src.application.auth_module.api.view.users.users import UserViewSet

router = Router()
router.register("", viewset=UserViewSet, basename="users")
urlpatterns = [
    path("", include(router.urls)),
    path("change/password/", UserChangePasswordView.as_view()),
    path('cargar-usuarios/', CargarUsuariosExcel.as_view(), name='cargar-usuarios'),
    path("graduados", GraduadosView.as_view()),
    path("graduados/<int:graduado_id>/", GraduadoView.as_view(), name="graduado"),
    path("graduados/Detail/<int:graduado_id>/", GraduadoDetailView.as_view(), name="graduado-detalle"),
    path("funcionarios", FuncionariosView.as_view()),
    path("funcionarios/<int:funcionario_id>/", FuncionarioView.as_view()),
]
