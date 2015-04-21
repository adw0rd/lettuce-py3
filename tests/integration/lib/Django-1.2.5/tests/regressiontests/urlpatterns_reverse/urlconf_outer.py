from django.conf.urls.defaults import *

from . import urlconf_inner


urlpatterns = patterns('',
    url(r'^test/me/$', urlconf_inner.inner_view, name='outer'),
    url(r'^inner_urlconf/', include(urlconf_inner.__name__))
)