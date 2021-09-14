from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.base import View
from .models import Customer , Product
from .models import Category
from .models import Order
from django.contrib.auth.hashers import make_password, check_password
from django.utils import translation
from django.utils.translation import get_language, activate, gettext




# Create your views here.

class index(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("/")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products =Product.get_all_products_by_id(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'index.html', data)

class search(View):
    def get(self, request):
        q = request.GET.get('search')
        if q:
            # products = Product.objects.filter(name__contains = q)
            products = [item for item in Product.objects.all() if q in item.name.lower() or q in item.description.lower() ]
            context = {'query':q, 'products':products}
        else:
            context = {}
        return render(request, "search.html", context)

class signup(View):
    def get(delf, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        
        #Validation

        value = {'first_name' : first_name,'last_name' : last_name,'phone' : phone,'email' : email}

        if len(phone) < 10:
            error_message = 'Enter valid number'
        elif len(email) < 4:
            error_message = 'Email must be 4 character'
        elif len(password) < 6:
            error_message = 'Password must be 6 character'
        elif customer.isExists():
            error_message = 'Email Address Already Taken'
        
        #Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values' : value
            }
        return render(request, 'signup.html', data)


class login(View):
    return_url = None
    def get(self, request):
        login.return_url = request.GET.get('return_url')
        return render(request, 'login.html') 
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['customer_name'] = customer.first_name
                if login.return_url:
                    return redirect('cart')
                else:
                    login.return_url = None
                    return redirect('home')                
            else:
                error_message = 'Email or Password invalid !!'

        else:
            error_message = 'Email or Password invalid !!'
        return render(request, 'login.html', {'error' : error_message})
        

        
def logout(request):
    request.session.clear()
    return redirect("/")

def category(request):
    return render(request, 'Category.html')
def Contact(request):
    return render(request, 'Contact.html')

class Grocery(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("Grocery")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(1)
        return render(request, 'Grocery.html', {'products' : products})

class Appliances(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("Appliances")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(4)
        return render(request, 'Appliances.html', {'products' : products})

class Beauty(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("Beauty")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(8)
        return render(request, 'Beauty.html', {'products' : products})

class Electronics(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("Electronics")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(6)
        return render(request, 'Electronics.html', {'products' : products})

class Fashion(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("Fashion")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(3)
        return render(request, 'Fashion.html', {'products' : products})

class HomeFurniture(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("HomeFurniture")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(5)
        return render(request, 'HomeFurniture.html', {'products' : products})

class Mobile(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("Mobile")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(2)
        return render(request, 'Mobile.html', {'products' : products})
          
class Toy(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("Toy")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
        products = None
        products = Product.get_all_products_by_id(9)
        return render(request, 'Toy.html', {'products' : products})   

    
class cart(View):
    def post(self,request):
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        delete = request.POST.get('delete')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1 
                elif delete:
                    cart.pop(product)
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        return redirect("cart")
    def get(self, request):
        cart = request.session.get('cart') 
        if not cart:
            request.session['cart'] = {}
            Products = None
        else:    
            ids = list(request.session.get('cart').keys())
            Products = Product.get_products_by_id(ids)
        return render(request, 'cart.html',{'products' : Products})

class checkout(View):
    def get(delf, request):
        cart = request.session.get('cart')
        ids = list(request.session.get('cart').keys())
        Products = Product.get_products_by_id(ids)
        return render(request, 'checkout.html',{'products' : Products})

    def post(self, request):
        #credential
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        #address
        street = request.POST.get('street')
        house = request.POST.get('houseno')
        region = request.POST.get('region')
        postal_code = request.POST.get('postalcode')
        #delivery method
        delivery_method = request.POST.get('delivery_method')
        #session
        customer = request.session.get('customer')
        name = request.session.get('customer_name')
        #cart 
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        total = request.POST.get('total')
        
        print(email, phone, street, house, region, postal_code, delivery_method, total)

        #saving into database in order model

        for product in products:
            order = Order(product = product,
                          customers = Customer(id = customer),                          
                          quantity = cart.get(str(product.id)),
                          price = product.price,
                          street = street,
                          house = house,
                          region = region,
                          postal_code = postal_code,
                          phone = phone,
                          payment_choice = delivery_method
            )
            
            order.placeOrder()
        
        request.session['cart'] = {}
        return redirect('home')

class orders(View):
    def get(self, request):
        return_url = None
        Customer = request.session.get('customer')
        orders = Order.get_orders_by_customers(Customer)
        login.return_url = request.GET.get('return_url')
        return render(request, 'orders.html',{'orders':orders})

def selectlanguage(request):
    if request.method == 'POST':
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        return HttpResponseRedirect("/"+lang)