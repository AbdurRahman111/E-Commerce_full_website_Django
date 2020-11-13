from django.db import models
from .product import Product
from .customer import Customerdata
import datetime

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.IntegerField()
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=15)
    price=models.IntegerField(default=0)
    name = models.CharField(max_length=300, default="")
    date=models.DateField(default=datetime.datetime.today)
    stutas=models.BooleanField(default=False)



    @staticmethod
    def get_product_by_customer_id(customer_id):
        return Order.objects.filter(customer=customer_id)

