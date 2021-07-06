from django.db import models

class ShippingPlaces(models.Model):
	name = models.CharField(max_length=50)
	shipping_price = models.IntegerField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Shipping To"
