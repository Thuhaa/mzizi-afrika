from django.urls import path
from . import views
import cart

urlpatterns = [
    path('', views.catalogue_view, name='catalogue'),
    path('shop/', views.shop_view, name='shop'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('contact_us/', views.contact_us_view, name='contact_us'),
    path('product/<str:mybrand>/', views.detail_view, name='product_details'),
    path('place_order/', views.place_order_view, name="place_order"),
    path('payment/', views.payment_view, name="payment"),
    path('complete/', views.order_received, name="complete"),
]

#path('add-to-cart/<str:mybrand>/', views.add_to_cart_view, name='add-to-cart')