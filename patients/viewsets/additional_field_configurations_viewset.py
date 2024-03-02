from rest_framework import permissions, viewsets

from patients.models import AdditionalFieldConfiguration
from patients.serializers import AdditionalFieldConfigurationSerializer


class AdditionalFieldConfigurationsViewSet(viewsets.ModelViewSet):
    queryset = AdditionalFieldConfiguration.objects.all()
    serializer_class = AdditionalFieldConfigurationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AdditionalFieldConfiguration.objects.filter(provider=self.request.user)