from django.contrib import admin
from django.urls import path, include
from main import views
from .views import signup, login, index, Grocery, Appliances, Beauty, Electronics, Fashion, HomeFurniture, Mobile, Toy, search, cart,checkout, orders
from .middlewares.auth import auth_middleware

admin.site.site_header = " login to Items.uz"
admin.site.site_title = "Welcome to Items Dashboard"
admin.site.index_title = "Welcome!!"

urlpatterns = [
    path ("", index.as_view(), name="home"),
    path ("Contact", views.Contact, name="Contact"),
    path ("signup", signup.as_view(), name="signup"),
    path ("login", login.as_view(), name="login"),
    path ("logout", views.logout, name="logout"),
    path ("Category", views.category, name="Category"),
    path ("Grocery", Grocery.as_view(), name="Grocery"),
    path ("Appliances", Appliances.as_view(), name="Appliances"),
    path ("Beauty", Beauty.as_view(), name="Beauty"),
    path ("Electronics", Electronics.as_view(), name="Electronics"),
    path ("Fashion", Fashion.as_view(), name="Fashion"),
    path ("HomeFurniture", HomeFurniture.as_view(), name="HomeFurniture"),
    path ("Mobile", Mobile.as_view(), name="Mobile"),
    path ("Toy", Toy.as_view(), name="Toy"),
    path ("search",search.as_view(), name="search"),
    path ("cart",cart.as_view(), name="cart"),
    path ("checkout",auth_middleware(checkout.as_view()), name="checkout"),
    path ("orders",auth_middleware(orders.as_view()), name="orders"),
    path('selectlanguage', views.selectlanguage, name="selectlanguage"),
]
