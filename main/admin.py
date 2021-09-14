from django.contrib import admin
from .models import Customer, Category, Product, Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id' , 'name' ]


# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product, AdminProduct)