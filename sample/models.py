from django.db import models

from django_2gis_maps.fields import AddressField, GeoLocationField
from django_2gis_maps.mixins import DoubleGisMixin


class SampleModel(DoubleGisMixin, models.Model):
    address = AddressField(max_length=255)
    geolocation = GeoLocationField(blank=True)

    def __str__(self):
        return self.address
