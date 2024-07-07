from django.db import models

from core.models import BaseModel

from apps.users.models import UserModel


class AutoParkModel(BaseModel):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['-id']

    name = models.CharField(max_length=20)
    manager = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='managed_parks')
    admin = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='administered_parks')
    salesperson = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='sales_parks')
    mechanic = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, related_name='mechanic_parks')

