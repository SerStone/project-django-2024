from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from core.enums.region_enum import Region
from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel

UserModel = get_user_model()


class AdvertisementModel(BaseModel):
    class Meta:
        db_table = 'advertisements'
        ordering = ['-id']

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    location = models.CharField(max_length=100, choices=Region.choices())
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='advertisements', null=True)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='advertisements', null=True)
    view_count = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    contact_email = models.EmailField(max_length=254, null=True, blank=True)
    contact_phone = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')], default='USD')

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

        AdvertisementViewLog.objects.create(advertisement=self, viewed_at=timezone.now())

    def get_views_last_days(self, days):
        start_date = timezone.now() - timezone.timedelta(days=days)
        return self.view_logs.filter(viewed_at__gte=start_date).count()

    def get_average_price_in_region(self):
        advertisements = AdvertisementModel.objects.filter(location=self.location)
        exchange_rates = {rate.currency: rate for rate in ExchangeRate.objects.all()}

        total_price = Decimal(0)
        count = 0

        for ad in advertisements:
            price = ad.price
            currency = ad.currency

            if currency != self.currency:
                if currency == 'UAH':
                    if self.currency in exchange_rates:
                        price = price / Decimal(exchange_rates[self.currency].buy)
                    else:
                        continue
                else:
                    if currency in exchange_rates:
                        price = price * Decimal(exchange_rates[currency].sale)
                    else:
                        continue

                    if self.currency != 'UAH' and self.currency in exchange_rates:
                        price = price / Decimal(exchange_rates[self.currency].buy)

            total_price += price
            count += 1

        if count == 0:
            return 0

        return total_price / count


class ExchangeRate(BaseModel):
    currency = models.CharField(max_length=3, choices=[('USD', 'USD'), ('EUR', 'EUR'), ('UAH', 'UAH')])
    base_currency = models.CharField(max_length=3, default='UAH')
    buy = models.DecimalField(max_digits=10, decimal_places=4)
    sale = models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('currency', 'base_currency')


class AdvertisementViewLog(models.Model):
    advertisement = models.ForeignKey(AdvertisementModel, on_delete=models.CASCADE, related_name='view_logs')
    viewed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-viewed_at']
