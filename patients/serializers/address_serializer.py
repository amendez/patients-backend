from rest_framework import serializers

from patients.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'address1', 'address2', 'city', 'state', 'zip_code', 'country']