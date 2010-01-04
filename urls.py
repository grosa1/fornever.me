﻿# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from fornever.views import *
from fornever.robots import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^files/', include('fornever.files.urls')),
    (r'^robocode/', include('fornever.robocode.urls')),
    
    (r'^$', index),
    
    (r'^login/', login),
    (r'^logout/', logout),
    
    # Error pages
    (r'^404/$', error_404),
    (r'^500/$', error_500),
    
    # Regular pages
    (r'^(.*\.html?)$', html),
    
    (r'^robots.txt$', robots_txt),
    (r'^sitemap.xml$', sitemap_xml),
    (r'^sitemap_main.xml$', sitemap_main_xml),
)
