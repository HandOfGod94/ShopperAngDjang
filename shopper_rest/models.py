from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """Product table"""
    name = models.CharField(null=False, unique=True, max_length=50)
    manufacturer = models.CharField(null=False, max_length=50)
    price = models.FloatField(null=False, validators=[MinValueValidator(0.0)])

    def __str__(self):
        return "<Product %s: %s>" % (self.id, self.name)


class Retailer(models.Model):
    """Retailer table"""
    name = models.CharField(null=False, unique=True, max_length=50)
    street_address = models.CharField(max_length=50)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)

    def __str__(self):
        return "<Retailer %s: %s>" % (self.id, self.name)


class SaleData(models.Model):
    """Schema for stoing data of each product sale from that shop"""
    product = models.ForeignKey(Product)
    retailer = models.ForeignKey(Retailer)
    bought_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    sold_quantity = models.IntegerField(validators=[MinValueValidator(0)])
