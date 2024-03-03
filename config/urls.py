from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from patients import views
from patients.viewsets import AddressesViewSet, UsersViewSet, PatientsViewSet, AdditionalFieldConfigurationsViewSet

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'patients', PatientsViewSet)
router.register(r'additional_field_configurations', AdditionalFieldConfigurationsViewSet)
router.register(r'addresses', AddressesViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path("login/", views.UserLoginView.as_view()),
]

urlpatterns += router.urls
