from django.urls import path
from inicio.views import inicio, crear_auto, listado_de_autos
urlpatterns = [
    path('inicio/',inicio,name='inicio'),
    #path('auto/crear/<marca>/<modelo>/',crear_auto),
    path('auto/',listado_de_autos,name='listado_de_autos'),
    path('auto/crear/',crear_auto,name='crear_auto'),
]