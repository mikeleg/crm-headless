from django.db import models

from infrastructure.models.customer import Customer


class Contact(models.Model):
    nickname = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    jobTitle = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, related_name="contacts", null=True
    )
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        db_table = "contact"
