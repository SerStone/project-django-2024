from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from core.models import BaseModel
from core.services.file_service import FileService

from apps.users.managers import UserManager


class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_premium = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(blank=True, upload_to=FileService.upload_avatar)
