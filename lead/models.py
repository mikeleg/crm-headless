import uuid
from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    legalname = models.CharField(max_length=100)
    vat = models.CharField(max_length=20)

    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=32)
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    geo = models.CharField(max_length=20, blank=True)

    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    pec = models.CharField(max_length=200, blank=True)
    sdi = models.CharField(max_length=20, blank=True)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "lead"
        verbose_name_plural = "leads"
        db_table = "lead"
