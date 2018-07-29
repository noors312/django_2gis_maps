import django
from django.contrib import admin

admin.autodiscover()

if django.get_version() >= '2.0.0':
    from django.urls import re_path as url
    from django.urls import include
else:
    from django.conf.urls import url, include
from sample.views import SampleFormView

urlpatterns = [
    # url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', SampleFormView.as_view()),
]
