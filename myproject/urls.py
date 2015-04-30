from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^css/(.*)$', 'cms_put.views.cssView'),
                       url(r'^(.*)$', "cms_put.views.mostrar"),
                       )
