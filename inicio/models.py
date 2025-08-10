from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    # anio = models.IntegerField()
    # precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} {self.modelo}"
# Create your models here.
#({self.anio}) - ${self.precio}