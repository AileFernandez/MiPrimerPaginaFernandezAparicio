from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),  
    path('pedido/', include('pedidos.urls', namespace='pedidos')),
    path('usuarios/', include('usuarios.urls')),
    path('about/', TemplateView.as_view(template_name='acercademi.html'), name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

