from rest_framework import serializers

from src.application.auth_module.models import CondicionesVulnerables

class CondicionesVulnerablesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CondicionesVulnerables
        fields = ("id","name")
        # exclude = ("userCreate", "userUpdate", "name","createdAt","updateAt", "visible","person")
