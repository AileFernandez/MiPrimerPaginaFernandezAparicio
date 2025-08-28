from django.urls import path
from . import views
from .views import lista_pedidos,nuevo_pedido,detalle_pedido,borrar_pedido

app_name = "pedidos"

urlpatterns = [
    path("nuevo/", views.nuevo_pedido, name="nuevo_pedido"),
    path("lista/", views.lista_pedidos, name="lista_pedidos"),
   # path("detalle/<int:pedido_id>/", detalle_pedido, name="detalle_pedido"),
    path("detalle/<int:pedido_id>", views.detalle_pedido, name="detalle_pedido"),
    path("borrar/<int:pk>/", views.borrar_pedido.as_view(), name="borrar_pedido"),
    path("actualizar/<int:pk>/", views.ActualizarPedido.as_view(), name="actualizar_pedido"),

]