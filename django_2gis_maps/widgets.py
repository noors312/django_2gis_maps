from django.conf import settings
from django.forms import widgets


class DoubleGisMapsAddressWidget(widgets.TextInput):
    """a widget that will place a google map right after the #id_address field"""
    template_name = "django_google_maps/widgets/map_widget.html"

    class Media:
        css = {
            'all': (settings.STATIC_URL +
                    'django_2gis_maps/css/2gis-maps-admin.css',)
        }
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js',
            'https://maps.api.2gis.ru/2.0/loader.js?pkg=full&skin=dark',
            settings.STATIC_URL + 'django_2gis_maps/js/2gis-maps-admin.js',
        )
