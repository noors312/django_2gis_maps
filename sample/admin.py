from django.contrib import admin
from django.forms.widgets import TextInput

from django_2gis_maps.admin import DoubleGisAdmin
from django_2gis_maps.widgets import DoubleGisMapsAddressWidget
from django_2gis_maps.fields import AddressField, GeoLocationField

from sample import models


class SampleModelAdmin(DoubleGisAdmin):
    pass


admin.site.register(models.SampleModel, SampleModelAdmin)
