from django.shortcuts import render
from .models import *

# Create your views here.

def store(request):
    products = Product.objects.all() # Obtendo todos os produtos
    context = {'products':products} # Enviando um dic para o template como contexto
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Cria ou obtem um pedido, se ele existir
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.ordered_item_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0} # Se o user não estiver logado, cria uma replica de um pedido

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Cria ou obtem um pedido, se ele existir
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.ordered_item_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0} # Se o user não estiver logado, cria uma replica de um pedido

    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)
