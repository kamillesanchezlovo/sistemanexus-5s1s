from rest_framework import serializers

class PresupuestoCreateSerializer(serializers.Serializer):
    plantillaId = serializers.IntegerField()
    escenario = serializers.CharField(max_length=50)

class MovimientoInventarioSerializer(serializers.Serializer):
    tipo = serializers.ChoiceField(choices=["entrada", "salida", "traslado"])
    itemId = serializers.IntegerField()
    cantidad = serializers.DecimalField(max_digits=12, decimal_places=2)
    origen = serializers.CharField(required=False, allow_blank=True)
    destino = serializers.CharField(required=False, allow_blank=True)
