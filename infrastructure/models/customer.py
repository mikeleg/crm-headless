from random import choices
from statistics import mode
from django.db import models

from core.enums import CUSTOMER_TYPE


class Customer(models.Model):

    nickname = models.CharField(max_length=200, blank=True)
    legalname = models.CharField(max_length=200)
    vat = models.CharField(max_length=20)

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=32)
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    geo = models.CharField(max_length=20, blank=True)

    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=200)
    pec = models.CharField(max_length=200, blank=True)
    sdi = models.CharField(max_length=20, blank=True)
    type = models.CharField(
        max_length=20,
        choices=CUSTOMER_TYPE,
        default=CUSTOMER_TYPE.CUSTOMER,
    )
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "customer"
        verbose_name_plural = "customers"
        db_table = "customer"
