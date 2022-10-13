from django.db import models


class CUSTOMER_TYPE(models.TextChoices):
    CUSTOMER = "customer", "customer"
    PROSPECT = "prospect", "prospect"
    LEAD = "lead", "lead"


class ADDRESS_TYPE(models.TextChoices):
    BILLING = "billing", "billing"
    SHIPPING = "shipping", "shipping"
    OTHER = "other", "other"
