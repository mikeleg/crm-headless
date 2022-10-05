from django.db import models


class CUSTOMER_TYPE(models.TextChoices):
    CUSTOMER = "customer", "customer"
    PROSPECT = "prospect", "prospect"
    LEAD = "lead", "lead"
