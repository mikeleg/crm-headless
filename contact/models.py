from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    default = models.BooleanField(default=False)
    jobTitle = models.CharField(max_length=100, blank=True)
    lead_id = models.IntegerField(null=True)
    account_id = models.IntegerField(null=True)

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        db_table = "contact"
