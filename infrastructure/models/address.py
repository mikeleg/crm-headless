from django.db import models

from core.enums import ADDRESS_TYPE


class Address(models.Model):
    nickname = models.CharField(max_length=50, null=True)
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    customer = models.ForeignKey(
        "Customer", on_delete=models.DO_NOTHING, related_name="addresses"
    )
    contact = models.ForeignKey(
        "Contact", on_delete=models.DO_NOTHING, related_name="addresses"
    )
    type = models.CharField(max_length=20, choices=ADDRESS_TYPE.choices, null=True)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "address"
        verbose_name_plural = "addresses"
        db_table = "address"
