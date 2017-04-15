from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'v0/$', views.getsubjects),
]