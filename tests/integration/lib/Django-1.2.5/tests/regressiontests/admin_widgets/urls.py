
from django.conf.urls.defaults import *
from . import widgetadmin

urlpatterns = patterns('',
    (r'^', include(widgetadmin.site.urls)),
)
