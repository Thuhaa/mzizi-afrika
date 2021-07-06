from django.contrib import admin
from .models import ShippingPlaces

class ShippingPlacesAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'name', 'shipping_price']
	class Meta:
		model = ShippingPlaces


admin.site.register(ShippingPlaces, ShippingPlacesAdmin)
# Register your models here.
