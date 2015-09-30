from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
                       url(r'^$', views.CountryFormView.as_view(), name='index'),
                       url(r'^(?P<country>[^/]+)$', views.CountryNewsView.as_view(), name='news'),
                       url(r'^(?P<country>[^/]+)/(?P<article>\d+)$', views.ArticleView.as_view(), name='article'),
                       )