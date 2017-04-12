from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<subject_t>[\w-]+)/$', views.subject),
    url(r'^(?P<subject_t>[\w-]+)/get_static_test/(?P<num>[1-6]+)/$', views.get_test, name='get static test'),
    url(r'^api/tasks/$', views.tasks_list),
    url(r'^api/tasks/(?P<pk>[0-9]+)/$', views.tasks_detail)
]