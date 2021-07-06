from django.db import models
from django.contrib.postgres.fields import ArrayField, HStoreField, JSONField
import random
from accounts.models import User

DISPLAY_CATEGORY_CHOICES = (
    ('New', 'New'),
    ('Top', 'Top'),
    ('Coming Soon', 'Coming Soon')
)


class Bag(models.Model):
    bags_id = models.AutoField
    brand = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=100, blank=True)
    picture = models.ImageField(upload_to='bag_pictures')
    discount_price = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now=True)
    in_stock = models.IntegerField(null=True, blank=True)
    eye_grasper = models.BooleanField(default=False)
    display_category = models.CharField(
        choices=DISPLAY_CATEGORY_CHOICES, default="New", max_length=20)

    class Meta:
        verbose_name_plural = "Bags"

    def __str__(self):
        return self.brand

#Create Order Models to ensure that all orders are recorded in the database
class Order(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    transaction_id = models.CharField(max_length=100, null=True)
    bags_ordered = ArrayField(models.CharField(max_length=50))
    total_amount = models.CharField(max_length=50, null=True)
    approved = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return self.transaction_id

class CurrentBuyer(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)
    class Meta:
        verbose_name_plural = "Current Buyers"

    def __str__(self):
        return self.phone

    def get_phone_number(self):
        return self.phone
