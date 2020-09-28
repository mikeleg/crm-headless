import uuid
from django.db import models
from core import fields


class Account(models.Model):

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    name = models.CharField(max_length=100)
    legalname = models.CharField(max_length=100)
    vat = models.CharField(max_length=20)

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=32)
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    geo = models.CharField(max_length=20)

    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    pec = models.CharField(max_length=200)
    sdi = models.CharField(max_length=20)

    type = models.CharField(max_length=10, choices=fields.CUSTOMER_TYPE)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"
        db_table = "account"
