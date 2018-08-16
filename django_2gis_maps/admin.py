from django.contrib import admin
from django.forms import TextInput

from django_2gis_maps.fields import AddressField, GeoLocationField
from django_2gis_maps.widgets import *


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            if self.multiple_markers:
                self.formfield_overrides[AddressField]['widget'] = DoubleGisMapsMultipleMarkersWidget
        except:
            raise
            # raise ("You missed multiple_markers ")
