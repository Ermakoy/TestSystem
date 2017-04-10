from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^math$', views.math),
    url(r'^api/tasks', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^math/get_test/(?P<num>[1-6]+)/$', views.get_test)
]