from rest_framework import permissions, viewsets

from patients.models import Address
from patients.serializers import AddressSerializer


class AddressesViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(patient__provider=self.request.user)