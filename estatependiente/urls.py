# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

# Load admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'estatependiente.views.home', name='home'),
    url(r'^categoria/(?P<category>\w+)/$','estatependiente.products.views.view_category',name='view_category'),
#    url(r'^producto/(?P<producto>\w+)/$','estatependiente.products.views.view_product',name='view_product'),
#    #Admin url
    url(r'^admin/', include(admin.site.urls)),
)
