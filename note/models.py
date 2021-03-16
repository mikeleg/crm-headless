from django.db import models
from account.models import Account


class Note(models.Model):
    description = models.TextField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "note"
        verbose_name_plural = "notes"
        db_table = "note"
