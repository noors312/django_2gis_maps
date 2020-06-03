from __future__ import unicode_literals

from django import template

register = template.Library()


@register.inclusion_tag("django_2gis_maps/map/map.html")
def render_map(instance, **kwargs):
    context = {
        'instance': instance,
        'geolocation': instance.get_location,
    }
    # return
    if kwargs:
        context.update(kwargs)
    return context
