from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?P<subject>[\w-]+)/$', views.subject),
    url(r'^api/tasks', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(?P<subs>[\w-]+)/(?P<subject>[\w-]+)/get_test/(?P<num>[1-6]+)/$', views.get_test)
]