from shop.models import Bag
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddBagForm
from .models import ShippingPlaces
from django.contrib import messages

def cart_view(request):
	cart = Cart(request)
	items_in_cart = []
	for bag in cart:
		items_in_cart.append(bag)
	number_of_items_in_cart = len(items_in_cart)
	print(number_of_items_in_cart)
	return render(request, 'cart/cart_view.html', {'cart':cart, 'number_of_items_in_cart':number_of_items_in_cart,})



@require_POST
def cart_add(request, bag_id):
	cart = Cart(request)
	bag = get_object_or_404(Bag, id=bag_id)
	form = CartAddBagForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(bag=bag,quantity=cd['quantity'],override_quantity=cd['override'])
		messages.success(request, ('{} was successfully added to cart'.format(bag.brand)))
	return redirect('/product/{}'.format(bag.brand))

@require_POST
def cart_remove(request, bag_id):
	cart = Cart(request)
	bag = get_object_or_404(Bag, id=bag_id)
	cart.remove(bag)
	messages.success(request, ('{} was successfully removed from cart'.format(bag.brand)))
	return redirect('cart')
