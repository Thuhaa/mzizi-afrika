from django.shortcuts import render, redirect, get_object_or_404
from .models import Bag, Order, CurrentBuyer
from django.http import JsonResponse
from cart.forms import CartAddBagForm
from cart.cart import Cart
import random
import json
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from decimal import Decimal



def catalogue_view(request):
	current_user = request.user
	cart = Cart(request)

	items_in_cart = []
	for bag in cart:
		items_in_cart.append(bag)
	number_of_items_in_cart = len(items_in_cart)
	bags = Bag.objects.all()
	new_bags = bags.filter(display_category="New")
	bags_list = []

	for bag in new_bags:
		if len(bags_list) < 4:
			bags_list.append(bag)

	context = {'bags_list':bags_list, 'current_user':current_user, 
	'number_of_items_in_cart':number_of_items_in_cart}

	return render(request, 'shop/catalogue.html', context)


def add_to_cart_from_shop(request):
	cart_product_form = CartAddBagForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(bag=bag,quantity=cd['quantity'],override_quantity=cd['override'])
		messages.success(request, ('{} was successfully added to cart.'.format(bag.brand)))
		return redirect('/product/{}'.format(bag.brand))


def shop_view(request):
	'''
	This is the shopview
	'''
	bags = Bag.objects.all()
	cart = Cart(request)
	items_in_cart = []
	for bag in cart:
		items_in_cart.append(bag)
	number_of_items_in_cart = len(items_in_cart)
	print(number_of_items_in_cart)
	cart_product_form = CartAddBagForm()

	context = {'bags':bags, 'cart_product_form': cart_product_form, 
	'number_of_items_in_cart':number_of_items_in_cart}

	return render(request, 'shop/shop.html', context)



def checkout_view(request):
	cart = Cart(request)
	items_in_cart = []
	for bag in cart:
		items_in_cart.append(bag)
		print(bag)
	number_of_items_in_cart = len(items_in_cart)
	if cart.get_total_price() <= 0:
		messages.success(request, ('Your cart is empty'))
		return redirect('cart')
	context = {'cart':cart, 'number_of_items_in_cart':number_of_items_in_cart}
	return render(request, 'shop/checkout.html', context)

"""
1. The following view is intended to be used by pay on delivery customers

"""
def place_order_view(request):
	cart = Cart(request)
	items_in_cart = []

	for bag in cart:
		items_in_cart.append(bag['bag'])
		print(bag['bag'])

	number_of_items_in_cart = len(items_in_cart)
	print(number_of_items_in_cart, items_in_cart)
		
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		phone_number = request.POST.get('phone_number')
		city = request.POST.get('city')
		bags_ordered = items_in_cart
		transaction_id = random.randint(1111111111,9999999999)
		total_amount = cart.get_total_price()
		order = Order.objects.create(first_name=first_name, last_name=last_name,
			phone = phone_number, city=city, transaction_id=transaction_id, 
			bags_ordered=bags_ordered, total_amount=total_amount)
		current_buyer = CurrentBuyer.objects.create(first_name=first_name, last_name=last_name,
			phone = phone_number, city=city)
		current_buyer.save()
		thephone = current_buyer.phone
		order.save()
		messages.success(request, ('Order has been placed successfully'))
		cart.clear()
		return HttpResponseRedirect('/payment')
# Remember to tie the request.session to the transaction_id


def contact_us_view(request):
	cart = Cart(request)
	items_in_cart = []
	for bag in cart:
		items_in_cart.append(bag)
	number_of_items_in_cart = len(items_in_cart)
	context = {'number_of_items_in_cart':number_of_items_in_cart}
	return render(request, 'shop/contact_us.html', context)



def detail_view(request, mybrand):
	cart_product_form = CartAddBagForm()
	cart = Cart(request)

	items_in_cart = []
	for bag in cart:
		items_in_cart.append(bag)
	number_of_items_in_cart = len(items_in_cart)

	thebag = Bag.objects.filter(brand=mybrand)
	allbags = Bag.objects.all()
	eyegraspers= allbags.filter(eye_grasper=True)

	context = {
	'thebag':thebag[0], 'eyegraspers':eyegraspers, 
	'cart_product_form': cart_product_form, 
	'number_of_items_in_cart':number_of_items_in_cart, 
	'cart':cart,
	'items_in_cart':items_in_cart
	}
	print(items_in_cart)

	return render(request, 'shop/detail_view.html', context)


def payment_view(request):
	cart = Cart(request)
	items_in_cart = []
	
	for bag in cart:
		items_in_cart.append(bag['bag'])
		print(bag['bag'])
	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name')
	phone_number = request.POST.get('phone_number')
	city = request.POST.get('city')
	transaction_id = random.randint(1111111111,9999999999)
	bags_ordered = items_in_cart
	total_amount = cart.get_total_price()
	number_of_items_in_cart = len(items_in_cart)
	order = Order.objects.create(first_name=first_name, last_name=last_name,
			phone = phone_number, city=city, transaction_id=transaction_id, 
			bags_ordered=bags_ordered, total_amount=total_amount)
	current_buyer = CurrentBuyer.objects.create(first_name=first_name, last_name=last_name,
			phone = phone_number, city=city)
	current_buyer.save()
	thephone = current_buyer.phone
	order.save()
	cart.clear()

	context = {'cart':cart,
	'order':order,
	'number_of_items_in_cart':number_of_items_in_cart,
	'transaction_id':transaction_id}

	return render(request, 'shop/payment.html', context)


def order_received(request):
	return render(request, 'shop/success.html')