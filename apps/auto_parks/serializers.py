from rest_framework import serializers

from apps.advertisements.serializers import AdvertisementSerializer
from apps.auto_parks.models import AutoParkModel
from apps.users.serializers import UserAutoParkSerializer, UserSerializer


class AutoParkWithOutCarsSerializer(serializers.ModelSerializer):
    advertisements = AdvertisementSerializer(many=True)
    manager = UserAutoParkSerializer()

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['manager'] = user
        return super().create(validated_data)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'manager', 'admin', 'salesperson', 'mechanic', 'created_at', 'updated_at','advertisements')
