from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PedidoForm, FormBuscarCliente
from .models import Pedido
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def nuevo_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST, request.FILES)  # 👈 importante incluir request.FILES
        if form.is_valid():
            form.save()
            return redirect("pedidos:lista_pedidos")
    else:
        form = PedidoForm()
    return render(request, "pedidos/nuevo_pedido.html", {"form": form})

def lista_pedidos(request):
    formulario = FormBuscarCliente(request.GET)

    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get("nombre")
        pedidos_buscados = Pedido.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        pedidos_buscados = Pedido.objects.all()

    return render(request, "pedidos/lista_pedidos.html", {
        "pedidos_buscados": pedidos_buscados,
        "formulario": formulario
    })

def detalle_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    return render(request, "pedidos/detalle_pedido.html", {"pedido": pedido})

class borrar_pedido(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = "pedidos/borrar_pedido.html"
    success_url = reverse_lazy("pedidos:lista_pedidos")

from django import forms

class ActualizarPedido(LoginRequiredMixin, UpdateView):
    model = Pedido
    template_name = "pedidos/actualizar_pedido.html"
    success_url = reverse_lazy("pedidos:lista_pedidos")
    fields = '__all__'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.enctype = "multipart/form-data"
        return form

