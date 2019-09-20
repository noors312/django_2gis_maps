### <In English>

`django_2gis_maps` is a simple application that provides the basic
hooks into django_2gis_maps V2 api for use in Django models from Django
version 1.11+.  

Starting with `django_2gis_maps` version (0.7.0), Django 1.11+ is
required because Django changed their widget template rendering system. 

I'm using this to allow someone from the admin panels to type a
freeform address, have the address geocoded on change and plotted
on the map. If the location is not 100% correct, the user can
drag the marker to the correct spot and the geo coordinates will
update.
###
-----
![alt tag](http://info.2gis.com/img/2gis_logo.png)
-----
INSTALLATION
-----
- `pip install git+https://github.com/NursErgesh/django_2gis_maps.git`
- `pip install django_2gis_maps`
------
USAGE:
------
- include the `django_2gis_maps` app in your `settings.py`
- create a model that has both an address field and geolocation field

  ```python
  from django.db import models
  from django_2gis_maps import fields as map_fields
  from django_2gis_maps.mixins import DoubleGisMixin
  class Rental(DoubleGisMixin,models.Model):
      address = map_fields.AddressField(max_length=200)
      geolocation = map_fields.GeoLocationField()
  ```

- in the `admin.py` include the following as a formfield_override

  ```python
  from django.contrib import admin
  from django_2gis_maps.admin import DoubleGisAdmin

  class RentalAdmin(DoubleGisAdmin):
      multiple_markers = False        # Here is your option
  ```
- in template include `{% load doublegis  %}` and use `{% render_map instanse %}` wherever you need
---
That should be all you need to get started.

I also like to make the geolocation field readonly in the admin so a user
(myself) doesn't accidentally change it to a nonsensical value. There is
validation on the field so you can't enter an incorrect value, but you could
enter something that is not even close to the address you intended.

When you're displaying the address back to the user, just request the map
using the geocoordinates that were saved in your model. Maybe sometime when
I get around to it I'll see if I can create a method that will build that
into the model.
