# Generated by Django 3.0.6 on 2020-07-06 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order_delivered'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='complete',
            new_name='approved',
        ),
    ]
