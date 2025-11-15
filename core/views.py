from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PresupuestoCreateSerializer, MovimientoInventarioSerializer

@api_view(["POST"])
def crear_presupuesto(request):
    ser = PresupuestoCreateSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"ok": False, "errors": ser.errors}, status=status.HTTP_400_BAD_REQUEST)

    data = ser.validated_data
    result = {
        "ok": True,
        "mensaje": "Presupuesto creado",
        "id": 123,  
        "payload": data,
    }
    return Response(result, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def movimiento_inventario(request):
    ser = MovimientoInventarioSerializer(data=request.data)
    if not ser.is_valid():
        return Response({"ok": False, "errors": ser.errors}, status=status.HTTP_400_BAD_REQUEST)

    data = ser.validated_data
    result = {
        "ok": True,
        "mensaje": "Movimiento registrado",
        "movimientoId": 987,
        "payload": data,
    }
    return Response(result, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def ping(request):
    return Response({"ok": True, "mensaje": "pong"}, status=status.HTTP_200_OK)
