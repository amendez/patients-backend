from geopy.geocoders import Nominatim
from django.db import models


class Address(models.Model):
    address1 = models.CharField(max_length=1024, blank=False, null=False)
    address2 = models.CharField(max_length=1024, blank=True, null=True)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=120,blank=False, null=False)
    state = models.CharField(max_length=120, blank=False, null=False)
    country = models.CharField(max_length=120, blank=False, null=False)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    patient = models.ForeignKey(
        "patients.Patient", related_name="addresses", null=True, on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.address1}, {self.city}, {self.state}"

    def execute_geocoding(self):
        try:
            geolocator = Nominatim(user_agent="Patients code challenge")
            location = geolocator.geocode(f"{self.address1}, {self.city}, {self.state}, {self.zip_code}, {self.country}")
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
                self.save()
        except Exception as e:
            print(f"Error while geocoding: {e}")
