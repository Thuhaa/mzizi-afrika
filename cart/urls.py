from django.urls import path
from . import views

urlpatterns = [
path('cart/', views.cart_view, name='cart'),
path('add/<int:bag_id>/', views.cart_add, name='cart_add'),
path('remove/<int:bag_id>/', views.cart_remove,name='cart_remove'),
]
