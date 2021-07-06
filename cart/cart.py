from decimal import Decimal
from django.conf import settings
from shop.models import Bag

class Cart(object):
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def __iter__(self):
		bag_ids = self.cart.keys()
		bags = Bag.objects.filter(id__in=bag_ids)
		cart = self.cart.copy()
		for bag in bags:
			cart[str(bag.id)]['bag'] = bag
		for item in cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def add(self, bag, quantity=1, override_quantity=False):
		bag_id = str(bag.id)
		if bag_id not in self.cart:
			self.cart[bag_id] = {'quantity': 0,'price': str(bag.price)}
			if override_quantity:
				self.cart[bag_id]['quantity'] = quantity
			else:
				self.cart[bag_id]['quantity'] += quantity
				self.save()


	def save(self):
		self.session.modified = True

		

	def remove(self, bag):
		bag_id = str(bag.id)
		if bag_id in self.cart:
			del self.cart[bag_id]
			self.save()

	

	def __len__(self):
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item
			in self.cart.values())

	def clear(self):
		del self.session[settings.CART_SESSION_ID]
		self.save()