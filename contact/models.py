from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=100, blank=True)
    default = models.BooleanField(default=False)
    jobTitle = models.CharField(max_length=100, blank=True)
