from django.conf.urls import patterns, url

from myapp import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<username>\w+)/$',views.welcome),
    url(r'^new_user$',views.create_user)
)