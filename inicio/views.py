from django.shortcuts import render, redirect 
from django.http import HttpResponse
from inicio.models import Auto
from inicio.forms import FormularioCrearAuto

def inicio(request):
    return render(request,'inicio.html')
# Create your views here.
# 1:24 hs min se explica como no hay que hacer un formulario 

#v1.
#def crear_auto(request, marca, modelo):
 #   auto= Auto(marca=marca, modelo=modelo)
  #  auto.save()
   # return render(request,'crear_autov1.html', {'auto':auto})
#v2.
def crear_auto(request):

    print(request.POST)

    if request.method == 'POST':
        formulario= FormularioCrearAuto(request.POST)
        if formulario.is_valid():
            data= formulario.cleaned_data
            auto= Auto(marca=data.get('marca'), modelo=data.get('modelo'))
            auto.save()
            return redirect('listado_de_autos')
    else:
        formulario= FormularioCrearAuto()
    return render(request,'crear_auto_v2.html', {'formulario':formulario})

def listado_de_autos(request):
    autos= Auto.objects.all()
    return render(request,'listado_de_autos.html',{'autos':autos})