from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'subject$', views.subject),
    url(r'test$', views.test),
]