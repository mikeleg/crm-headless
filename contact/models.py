from django.db import models
from account.models import Account


class Contact(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, blank=True)
    default = models.BooleanField(default=False)
    jobTitle = models.CharField(max_length=100, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="contacts")

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "contact"
        verbose_name_plural = "contacts"
        db_table = "contact"

    def __str__(self) -> str:
        return f"{self.surname} {self.name}"