from django import forms
from sample.models import SampleModel
from django_2gis_maps.widgets import GoogleMapsAddressWidget


class SampleForm(forms.ModelForm):

    class Meta(object):
        model = SampleModel
        fields = ['address', 'geolocation']
        widgets = {
            "address": GoogleMapsAddressWidget,
        }
