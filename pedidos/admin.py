from django.contrib import admin
from .models import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "destino", "email", "fecha_viaje", "cantidad_personas", "creado_en")
    list_filter = ("destino", "creado_en")
    search_fields = ("nombre", "email", "destino")

