from django.contrib import admin
from django.forms import TextInput

from django_2gis_maps.fields import AddressField, GeoLocationField
from django_2gis_maps.widgets import DoubleGisMapsAddressWidget


class DoubleGisAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {
            'widget': DoubleGisMapsAddressWidget
        },
        GeoLocationField: {
            'widget': TextInput(attrs={
                'readonly': 'readonly'
            })
        },
    }
