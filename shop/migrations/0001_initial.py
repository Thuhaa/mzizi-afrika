# Generated by Django 3.0.6 on 2020-07-06 17:16

import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('color', models.CharField(blank=True, max_length=100)),
                ('picture', models.ImageField(upload_to='bag_pictures')),
                ('discount_price', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.CharField(blank=True, max_length=100)),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('in_stock', models.IntegerField(blank=True, null=True)),
                ('eye_grasper', models.BooleanField(default=False)),
                ('display_category', models.CharField(choices=[('New', 'New'), ('Top', 'Top'), ('Coming Soon', 'Coming Soon')], default='New', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Bags',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('bags_ordered', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), size=None)),
                ('total_amount', models.CharField(max_length=50, null=True)),
                ('complete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
