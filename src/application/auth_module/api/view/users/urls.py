from django.urls import path, re_path
from .users import CargarUsuariosExcel, FuncionarioRolesView, FuncionariosView, GraduadoDetailView, GraduadosView, UserChangePasswordView

from django.conf.urls import include


from src.application.auth_module.api.view.users.route import Router
from src.application.auth_module.api.view.users.users import UserViewSet

router = Router()
router.register("", viewset=UserViewSet, basename="users")
urlpatterns = [
    path("", include(router.urls)),
    path("change/password/", UserChangePasswordView.as_view()),
    path('cargar-usuarios/', CargarUsuariosExcel.as_view(), name='cargar-usuarios'),
    re_path("graduados/?(?P<graduado_id>[0-9]+)?/$", GraduadosView.as_view(), name="graduados"),
    re_path("funcionarios/?(?P<funcionario_id>[0-9]+)?/$", FuncionariosView.as_view(), name="funcionarios"),
    path("funcionarios/roles/<int:funcionario_id>/", FuncionarioRolesView.as_view()),
    path("detail/<int:graduado_id>/", GraduadoDetailView.as_view(), name="user-detail"),
]
