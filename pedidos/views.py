from django.shortcuts import render, redirect
from .forms import PedidoForm
from .models import Pedido

def nuevo_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedidos:lista_pedidos")
    else:
        form = PedidoForm()
    return render(request, "pedidos/nuevo_pedido.html", {"form": form})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, "pedidos/lista_pedidos.html", {"pedidos": pedidos})
