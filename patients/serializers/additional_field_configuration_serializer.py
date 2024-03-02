from rest_framework import serializers

from patients.models import AdditionalFieldConfiguration


class AdditionalFieldConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFieldConfiguration
        fields = ['id', 'name', 'type', 'provider']
        read_only_fields = ['id', 'provider']

    def create(self, validated_data):
        validated_data['provider'] = self.context['request'].user
        return super().create(validated_data)