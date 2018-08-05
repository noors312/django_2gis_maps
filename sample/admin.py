from django.contrib import admin

from django_2gis_maps.admin import DoubleGisAdmin
from sample import models


class SampleModelAdmin(DoubleGisAdmin):
    multiple_markers = False


admin.site.register(models.SampleModel, SampleModelAdmin)
