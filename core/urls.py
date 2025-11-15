from django.urls import path
from . import views

urlpatterns = [
    path("ping/", views.ping, name="ping"),
    path("presupuestos/", views.crear_presupuesto, name="crear_presupuesto"),
    path("inventario/movimientos/", views.movimiento_inventario, name="movimiento_inventario"),
]
