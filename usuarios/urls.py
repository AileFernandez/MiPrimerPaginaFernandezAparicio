from django.urls import path
from usuarios.views import iniciar_sesion, registro, perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path("registro/", registro, name="registro"),
    path('perfil/', perfil, name='perfil'),
    path('cerrar-sesion/', LogoutView.as_view(template_name="cerrar_sesion.html"), name='cerrar_sesion')

]
