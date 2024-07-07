from rest_framework import serializers

from .models import PropositionModel


class PropositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropositionModel
        fields = ['id', 'user', 'brand', 'message', 'created_at', 'is_reviewed']
        read_only_fields = ['id', 'user', 'created_at', 'is_reviewed']