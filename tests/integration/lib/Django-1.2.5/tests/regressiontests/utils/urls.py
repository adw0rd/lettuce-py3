from django.conf.urls.defaults import *

from . import views

urlpatterns = patterns('',
    (r'^xview/$', views.xview),
    (r'^class_xview/$', views.class_xview),
)
