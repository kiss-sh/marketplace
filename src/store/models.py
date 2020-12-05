from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    name = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    
    def __str__(self):
    	return self.name

class Product(models.Model):
	name = models.CharField(max_length = 200, null = True)
	price = models.FloatField()
	is_digital = models.BooleanField(default = False, null = True, blank = True)
	#image = 

	def __str__(self):
		return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, blank = True, null = True) # Se um cliente for apagado, não apaga o pedido
    date_orded = models.DateTimeField(auto_now_add = True)
    complete = models.BooleanField(default = False, null = True, blank = False)
    transaction_id = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return str(self.id) # Id (inteiro), convertido para string

class Ordered_item(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL, null = True)
    quantity = models.IntegerField(default = 0, null = True, blank = True)
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'Ordered Items'


class Shipping_address(models.Model):
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