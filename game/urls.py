from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index),
    path('hello', views.hello_world),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
