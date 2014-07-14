from django.conf.urls import patterns, include, url
from household import views

urlpatterns = patterns('',
    url(r'^$',  views.index, name='index'),
)