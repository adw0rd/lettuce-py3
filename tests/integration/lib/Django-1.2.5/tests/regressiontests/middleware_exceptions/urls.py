# coding: utf-8
from django.conf.urls.defaults import *

from . import views

urlpatterns = patterns('',
    (r'^$', views.index),
)
