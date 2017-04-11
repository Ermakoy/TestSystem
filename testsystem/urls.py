from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<subject>[\w-]+)/$', views.subject),
    url(r'^(?P<subs>[\w-]+)/(?P<subject>[\w-]+)/get_test/(?P<num>[1-6]+)/$', views.get_test),
    url(r'^api/tasks/$', views.tasks_list)
]