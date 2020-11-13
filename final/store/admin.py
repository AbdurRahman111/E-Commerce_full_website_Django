from django.contrib import admin

# Register your models here.
from .models.product import Product
from .models.category import Category
from .models.customer import Customerdata
from .models.order import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class Customer_data1(admin.ModelAdmin):
    list_display = ['first_name' , 'last_name' , 'phone']

class Customer_order(admin.ModelAdmin):
    list_display = ['product' , 'customer' , 'phone']


admin.site.register(Product , AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customerdata, Customer_data1)
admin.site.register(Order , Customer_order)


