from django.contrib import admin
from .models import *
from django.utils.html import format_html

class BagAdmin(admin.ModelAdmin):
	def image_tag(self, obj):
		return format_html('<img src="{}" style="width:40px;" />'.format(obj.picture.url))
	image_tag.short_description = 'Picture'

	list_display = ['__str__', 'image_tag', 'color', 'discount_price', 'price', 'date_posted', 'display_category', 'in_stock']
	class Meta:
		model = Bag
class OrderAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'transaction_id','first_name', 'last_name', 'city', 'phone', 'bags_ordered', 'total_amount', 'approved', 'delivered']
	class Meta:
		model = Order

class CurrentBuyerAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'first_name', 'last_name', 'city', 'phone']
	class Meta:
		model = CurrentBuyer

			


admin.site.register(Bag, BagAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CurrentBuyer, CurrentBuyerAdmin)
admin.site.site_header = 'MZIZI AFIKA'
# Register your models here.
