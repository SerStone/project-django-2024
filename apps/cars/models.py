from django.core import validators as V
from django.db import models

from core.enums.brand_enum import CarBrand
from core.models import BaseModel
from core.services.file_service import FileService

from apps.advertisements.models import AdvertisementModel
from apps.cars.managers import CarManager

from .choices.body_type_choices import BodyTypeChoices
from .choices.condition_type_choices import ConditionTypeChoices


class CarModel(BaseModel):
    class Meta:
        db_table = 'car'
        ordering = ('-id',)

    brand = models.CharField(max_length=100, choices=CarBrand.choices())
    model_type = models.CharField(max_length=20)
    condition_type = models.CharField(max_length=20, choices=ConditionTypeChoices.choices)
    year = models.IntegerField(validators=[V.MinValueValidator(1900), V.MaxValueValidator(2024)])
    body_type = models.CharField(max_length=9, choices=BodyTypeChoices.choices)
    car_photo = models.ImageField(blank=True, upload_to=FileService.upload_car_photo)
    advertisement = models.OneToOneField(AdvertisementModel, on_delete=models.CASCADE, related_name='car')

    objects = CarManager()
