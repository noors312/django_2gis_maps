from django.contrib import admin

from django_2gis_maps.admin import DoubleGisAdmin
from sample import models


class SampleModelAdmin(DoubleGisAdmin):
    pass
    # multiple_markers = True


admin.site.register(models.SampleModel, SampleModelAdmin)
