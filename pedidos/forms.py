from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    fecha_viaje = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = Pedido
        fields = ["nombre", "email", "destino", "fecha_viaje", "cantidad_personas", "mensaje", "imagen"]  
        widgets = {
            "mensaje": forms.Textarea(attrs={"rows": 4, "placeholder": "Detalles, preferencias o preguntas..."}),
            "cantidad_personas": forms.NumberInput(attrs={"min": 1}),
        }

class FormBuscarCliente(forms.Form):
    nombre = forms.CharField(
        required=False,
        label="Nombre del cliente",
        widget=forms.TextInput(attrs={"placeholder": "Ingrese el nombre"})
    )
