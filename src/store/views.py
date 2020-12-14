from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime

from .models import *
from .utils import cookie_cart, cart_data

def store(request):
    data = cart_data(request)
    cartItems = data['cartItems']

    products = Product.objects.all() # Obtendo todos os produtos
    context = {'products':products, 'cartItems':cartItems} # Enviando um dic para o template como contexto
    return render(request, 'store/store.html', context)

def cart(request):
    data = cart_data(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request):
    
    data = cart_data(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

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
