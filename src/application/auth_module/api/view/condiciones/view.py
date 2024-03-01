from rest_framework.response import Response
from rest_framework import status
from configs.helpers.PaginationView import DecoratorPaginateView

from rest_framework.response import Response
from rest_framework.views import APIView
from src.application.auth_module.api.serializers.condiciones.codiciones_serializers import CondicionesVulnerablesSerializers
from src.application.auth_module.models import CondicionesVulnerables

class CondicionesVulnerablesView(APIView):
    @DecoratorPaginateView
    def get(self, request, *args, **kwargs):
        try:
            condiciones = CondicionesVulnerables.objects.all()
            serializer = CondicionesVulnerablesSerializers(condiciones, many=True)
            return serializer.data
        except Exception as e :
           return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       