# orders_app/urls.py
from django.urls import path
from .views import OrderListCreateView, OrderDetailView

urlpatterns = [
    path('', OrderListCreateView.as_view(), name='orders-list-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
