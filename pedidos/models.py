from django.db import models

class Pedido(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    destino = models.CharField(max_length=150)
    fecha_viaje = models.DateField(null=True, blank=True)
    cantidad_personas = models.PositiveIntegerField(default=1)
    mensaje = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.destino} ({self.creado_en.date()})"
