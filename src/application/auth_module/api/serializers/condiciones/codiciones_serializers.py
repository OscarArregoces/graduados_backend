from rest_framework import serializers

from src.application.auth_module.models import CondicionVulnerable

class CondicionesVulnerablesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CondicionVulnerable
        fields = ("id","name")
        # exclude = ("userCreate", "userUpdate", "name","createdAt","updateAt", "visible","person")
