from pyexpat import model
from rest_framework import serializers
from src.application.auth_module.api.serializers.user.users_serializers import UserSerializers

from src.application.auth_module.models import Carrera

class CarreraSerializers(serializers.ModelSerializer):
    # user_id = UserSerializers(read_only=True, many=True)
      
    class Meta:
        model = Carrera
        exclude = ("userCreate", "userUpdate", "name","createdAt","updateAt", "visible","person")
        # fields = '__all__'