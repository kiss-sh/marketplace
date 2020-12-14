import json
from .models import *

# Arquivo com a lógica do carrinho

def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        '''Se não tiver o cookie, cria um dic vazio
               (evita erro do usuário acessando a página pela primeira vez, sem cookie)''' 
        cart = {}

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':True} # Se o user não estiver logado, cria uma replica/representação de um pedido
    cartItems = order['get_cart_items']

    for i in cart:
        # try - se o produto existir
        try:
            cartItems += cart[i]['quantity']
            # i = product id

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            # Valores do carrinho atualizados (valor total e total de itens)
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            # Representação de um item
            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'image_url':product.image_url,
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total,
                }
            items.append(item) # Append do item na lista items (linha 41)
        except:
            # Evita dar erro se o produto for removido do bd
            pass
    return {'cartItems':cartItems, 'order':order, 'items':items}

# Dados do carrinho
def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        # Cria ou obtem um pedido, se ele existir
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.ordered_item_set.all()
        cartItems = order.get_cart_items
    else:
        cookie_data = cookie_cart(request)
        cartItems = cookie_data['cartItems']
        order = cookie_data['order']
        items = cookie_data['items']
    return {'cartItems':cartItems ,'order':order, 'items':items}