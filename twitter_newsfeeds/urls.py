from django.conf.urls import include, url
from django.contrib import admin






urlpatterns = [url(r'^$', include('newsfeeds.urls')),
               url(r'^admin/', include(admin.site.urls)),
               url(r'^news/', include('newsfeeds.urls')),
               ]
