from django.db import models

# Create your models here.
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE , default=1)
    description=models.CharField(max_length=300, default="")
    image=models.ImageField(upload_to='uploads/product')

    @staticmethod
    def get_all_product_id(cartid):
        return Product.objects.filter(id__in=cartid)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_categoryID(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_product()
