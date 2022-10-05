from django.db import models

from infrastructure.models.customer import Customer


class Note(models.Model):
    description = models.TextField()
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, related_name="notes", null=True
    )
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "note"
        verbose_name_plural = "notes"
        db_table = "note"
