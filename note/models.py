from django.db import models


class Note(models.Model):
    name = models.TextField()
    lead_id = models.IntegerField(null=True)
    account_id = models.IntegerField(null=True)
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "note"
        verbose_name_plural = "notes"
        db_table = "note"
