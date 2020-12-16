from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model): # Cliente
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True) #CASCADE: Se o objeto referenciado for excluido, exclua os obj que tem referencias a ele
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    
    def __str__(self):
    	return self.name

class Genre(models.Model): # Gênero do Filme
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name 

class Product(models.Model): # Produtos (filmes)
    name = models.CharField(max_length = 200, null = True)
    genre = models.ManyToManyField(Genre)
    price = models.FloatField()
    image = models.ImageField(null = True, blank = True)

    #TODO
    #description
    #stock

    def __str__(self):
        return self.name

    @property
    def image_url(self): # Caso o produto não tenha uma img
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model): # Pedidos
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank = True, null = True) # Se um cliente for apagado, não apaga o pedido
    date_orded = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return str(self.id) # Id (inteiro), convertido para string

    @property
    def shipping(self):
        shipping = True
        #ordered_items = self.ordered_items.set.all()
        return shipping

    @property
    def get_cart_total(self): # Valor total de produtos no carrinho
        ordered_items = self.ordered_item_set.all() # Todos os itens pedidos
        total = sum([item.get_total for item in ordered_items]) # Calcula o valor total de get_total
        return total

    @property
    def get_cart_items(self): # Items no carrinho
        ordered_items = self.ordered_item_set.all() # Todos os itens pedidos
        total = sum([item.quantity for item in ordered_items]) # Total de itens no carrinho
        return total

class Ordered_item(models.Model): # Itens pedidos
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Ordered Items'

    @property
    def get_total(self): # Valor total = preço do produto * quantidade
        total = self.product.price * self.quantity
        return total

class Shipping_address(models.Model): # Endereço de entrega (frete)
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    address = models.CharField(max_length = 200, null = False)
    city = models.CharField(max_length = 200, null = False)
    state = models.CharField(max_length = 200, null = False)
    zipcode = models.CharField(max_length = 200, null = True)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "Shipping Adress"

    def __str__(self):
        return self.address