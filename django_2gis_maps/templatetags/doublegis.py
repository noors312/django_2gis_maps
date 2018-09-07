from __future__ import unicode_literals

from math import floor

from django import template
from django.contrib.messages import constants as message_constants
from django.template import Context
from django.utils import six
from django.utils.safestring import mark_safe

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
