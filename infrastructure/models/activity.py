from django.db import models

from infrastructure.models.customer import Customer


class Activity(models.Model):
    description = models.TextField()
    due_date = models.DateTimeField()
    customer = models.ForeignKey(
        Customer, on_delete=models.DO_NOTHING, related_name="activities", null=True
    )
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "activity"
        verbose_name_plural = "activities"
        db_table = "activity"
