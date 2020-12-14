from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *

# Create your views here.

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        # Cria ou obtem um pedido, se ele existir
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.ordered_item_set.all()
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':True}
        cartItems = order['get_cart_items']

    products = Product.objects.all() # Obtendo todos os produtos
    context = {'products':products, 'cartItems':cartItems} # Enviando um dic para o template como contexto
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Cria ou obtem um pedido, se ele existir
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.ordered_item_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':True} # Se o user não estiver logado, cria uma replica de um pedido
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Cria ou obtem um pedido, se ele existir
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.ordered_item_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':True} # Se o user não estiver logado, cria uma replica de um pedido
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html', context)

def updateItem(request):

    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)

    ordered_item, created = Ordered_item.objects.get_or_create(order=order, product=product)

    if action == 'add':
        ordered_item.quantity = (ordered_item.quantity + 1)
    elif action == 'remove':
        ordered_item.quantity = (ordered_item.quantity - 1)

    ordered_item.save()

    if ordered_item.quantity <= 0:
        ordered_item.delete()

    return JsonResponse('item adicionado', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            Shipping_address.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],
            )

    else:
        print('Usuário não está logado...')
    return JsonResponse('Pagamento realizado', safe=False)
