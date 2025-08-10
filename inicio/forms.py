from django import forms

class FormularioCrearAuto(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField(max_length=30)
    