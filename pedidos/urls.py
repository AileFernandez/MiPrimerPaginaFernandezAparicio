from django.urls import path
from . import views

app_name = "pedidos"

urlpatterns = [
    path("nuevo/", views.nuevo_pedido, name="nuevo_pedido"),
    path("lista/", views.lista_pedidos, name="lista_pedidos"),
]