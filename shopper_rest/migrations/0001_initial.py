# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 08:44
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('manufacturer', models.CharField(max_length=50)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Retailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('street_address', models.CharField(max_length=50)),
                ('locality', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SaleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bought_quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('sold_quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopper_rest.Product')),
                ('retailer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopper_rest.Retailer')),
            ],
        ),
    ]