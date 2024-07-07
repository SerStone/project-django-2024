from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel

UserModel = get_user_model()


class PropositionModel(BaseModel):
    class Meta:
        db_table = 'propositions'
        ordering = ['-id']
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='propositions')
    brand = models.CharField(max_length=100)
    message = models.TextField(default="Your request is being processed.")
    created_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)
