from django.conf import settings
from django.forms import widgets


class DoubleGisMapsAddressWidget(widgets.TextInput):
    """a widget that will place a google map right after the #id_address field"""
    template_name = "django_2gis_maps/widgets/map_widget.html"

    class Media:
        css = {
            'all': (settings.STATIC_URL +
                    'django_2gis_maps/css/adminMap.css',)
        }
        js = (
            'https://code.jquery.com/jquery-latest.min.js',
            'https://maps.api.2gis.ru/2.0/loader.js?pkg=full&skin=dark',
            settings.STATIC_URL + 'django_2gis_maps/js/addMarkers.js',
            settings.STATIC_URL + 'django_2gis_maps/js/adminMap.js',
        )


class DoubleGisMapsMultipleMarkersWidget(widgets.TextInput):
    template_name = "django_2gis_maps/widgets/multiple_markers_widget.html"

    class Media:
        css = {
            'all': (settings.STATIC_URL +
                    'django_2gis_maps/css/adminMapMultipleMarkers.css',)
        }
        js = (
            'https://code.jquery.com/jquery-latest.min.js',
            'https://maps.api.2gis.ru/2.0/loader.js?pkg=full&skin=dark',
            settings.STATIC_URL + 'django_2gis_maps/js/addMarkers.js',
            settings.STATIC_URL + 'django_2gis_maps/js/adminMapMultipleMarkers.js',
        )
