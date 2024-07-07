from django.db.transaction import atomic

from rest_framework import serializers

from core.enums.region_enum import Region

from apps.advertisements.models import AdvertisementModel
from apps.cars.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'model_type', 'body_type', 'condition_type', 'year', 'created_at', 'updated_at',
                  'car_photo')


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('car_photo',)
        extra_kwargs = {
            'car_photo': {
                'required': True
            }
        }


class AdvertisementSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = AdvertisementModel
        fields = ('id', 'title', 'description', 'location', 'user', 'car', 'price', 'currency', 'is_active',
                  'contact_email', 'contact_phone')

        read_only_fields = ('id', 'is_active')

    @atomic
    def create(self, validated_data: dict):
        car = validated_data.pop('car')
        advertisement = AdvertisementModel.objects.create(**validated_data)
        CarModel.objects.create(**car, advertisement=advertisement)
        # EmailService.register(user)
        return advertisement

    @atomic
    def update(self, instance, validated_data: dict):
        car_data = validated_data.pop('car', None)
        if car_data:
            car_instance = instance.car
            for attr, value in car_data.items():
                setattr(car_instance, attr, value)
            car_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class PremiumAdvertisementSerializer(AdvertisementSerializer):
    view_count = serializers.IntegerField(read_only=True)
    views_last_day = serializers.SerializerMethodField()
    views_last_week = serializers.SerializerMethodField()
    views_last_month = serializers.SerializerMethodField()
    average_price_in_region = serializers.SerializerMethodField()

    class Meta(AdvertisementSerializer.Meta):
        fields = AdvertisementSerializer.Meta.fields + (
            'view_count', 'views_last_day', 'views_last_week', 'views_last_month', 'average_price_in_region'
        )

    def get_views_last_day(self, obj):
        return obj.get_views_last_days(1)

    def get_views_last_week(self, obj):
        return obj.get_views_last_days(7)

    def get_views_last_month(self, obj):
        return obj.get_views_last_days(30)

    def get_average_price_in_region(self, obj):
        return obj.get_average_price_in_region()

