from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False

class Category(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='users/%Y/%m/', default="")

    def addProduct(self):
        self.save()

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_id(category_id):
        return Product.objects.filter(category = category_id)


payment_method =[
    ("Home delivery", "Home delivery"),
    ("Take away", "Take away")
]

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, default=None)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=None)
    street = models.CharField(max_length=50, default='',blank=True)
    house = models.CharField(max_length=50, default='',blank=True)
    region = models.CharField(max_length=50, default='',blank=True)
    postal_code = models.CharField(max_length=10, default='',blank=True)
    phone = models.CharField(max_length=13,default='',blank=True)
    payment_choice = models.CharField(max_length=30, choices=payment_method, default=1)
    date  = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customers(customer_id):
        return Order \
        .objects \
        .filter(customers = customer_id) \
        .order_by('-date')