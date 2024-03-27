from rest_framework import serializers
from decimal import Decimal
from src.application.eventos.models.models import BienEquipo, MaterialSuministro, Personal, Presupuesto


class PresupuestoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_presupuesto = serializers.DecimalField(max_digits=15, decimal_places=2 ,read_only=True)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['total_presupuesto'] = Decimal(ret['total_presupuesto'])
        return ret

class TipoPresupuestoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # presupuesto = PresupusetoSerializer(read_only=True)
    item = serializers.CharField(read_only=True)
    cantidad = serializers.IntegerField(read_only=True)
    valor_unitario = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    inversion_uniguajira = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    especie_uniguajira = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    inversion_cofinanciador = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    especie_cofinanciador = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    nombre = serializers.CharField(read_only=True)
    valor = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['valor_unitario'] = Decimal(ret['valor_unitario'])
        ret['inversion_uniguajira'] = Decimal(ret['inversion_uniguajira'])
        ret['especie_uniguajira'] = Decimal(ret['especie_uniguajira'])
        ret['inversion_cofinanciador'] = Decimal(ret['inversion_cofinanciador'])
        ret['especie_cofinanciador'] = Decimal(ret['especie_cofinanciador'])
        ret['valor'] = Decimal(ret['valor'])
        return ret

class PresupuestoCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Presupuesto
        fields = "__all__"
        
class BienEquipoCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = BienEquipo
        fields = "__all__"
        
class MaterialSuministroCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MaterialSuministro
        fields = "__all__"
        
class PersonalCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Personal
        fields = "__all__"

class PresupuestoPayloadValidateSerializer(serializers.Serializer):
    bienesEquipos = TipoPresupuestoSerializer(many=True)
    materialesSuministros = TipoPresupuestoSerializer(many=True)
    personal = TipoPresupuestoSerializer(many=True)
    totalPresupuesto = serializers.DecimalField(max_digits=15, decimal_places=2)

    def validate(self, data):
        # Validar que se proporcionen los campos requeridos
        for campo in ['bienesEquipos', 'materialesSuministros', 'personal', 'totalPresupuesto']:
            if campo not in data:
                raise serializers.ValidationError(f"El campo '{campo}' es requerido")
        
        # Validar que los campos 'bienesEquipos', 'materialesSuministros', 'personal' sean listas
        for campo in ['bienesEquipos', 'materialesSuministros', 'personal']:
            if not isinstance(data[campo], list):
                raise serializers.ValidationError(f"El campo '{campo}' debe ser una lista")

        # Validar que el campo 'totalPresupuesto' sea un número
        if not isinstance(data['totalPresupuesto'], (int, float)):
            raise serializers.ValidationError("El campo 'totalPresupuesto' debe ser un número")
        return data