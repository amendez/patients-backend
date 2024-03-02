from rest_framework import serializers

from patients.models import AdditionalField


class ConciseAdditionalFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalField
        fields = ['id', 'name', 'value']