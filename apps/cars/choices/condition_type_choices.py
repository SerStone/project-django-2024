from django.db import models


class ConditionTypeChoices(models.TextChoices):
    New = "New"
    Used = "Used"
    Unregistered = "Unregistered"
    after_accident = "After Accident"
