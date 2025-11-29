# ecommerce_backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    # Authentication
    path('api/auth/', include('accounts_app.urls')),

    # Products
    path('api/products/', include('products_app.urls')),

    # Cart
    path('api/cart/', include('cart_app.urls')),

    # Orders
    path('api/orders/', include('orders_app.urls')),
]
