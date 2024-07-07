from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from core.services.email_service import EmailService

from apps.advertisements.serializers import AdvertisementSerializer
from apps.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'first_name', 'last_name', 'age', 'avatar')


class ProfileAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('avatar',)
        extra_kwargs = {
            'avatar': {
                'required': True
            }
        }


class UserAutoParkSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'last_login', 'profile',
        )
        read_only_fields = ('id', 'is_active', 'is_seller', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    advertisements = AdvertisementSerializer(many=True, required=False)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_seller', 'is_premium', 'is_active', 'is_staff', 'is_superuser', 'last_login', 'created_at',
            'updated_at', 'profile', 'advertisements',
        )
        read_only_fields = ('id', 'is_active', 'is_seller', 'is_premium', 'is_staff', 'is_superuser', 'last_login', 'created_at', 'updated_at')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        EmailService.register(user)
        return user
