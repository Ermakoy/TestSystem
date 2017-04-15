from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<subject_t>[\w-]+)/$', views.subject),
    url(r'^(?P<subject_t>[\w-]+)/get_static_test/(?P<num>[1-6]+)/$', views.get_static_test, name='get static test'),
    url(r'^(?P<subject_t>[\w-]+)/get_static_test/(?P<num>[1-6]+)/(?P<answer_t>[\w-]+)/$', views.check_static_test),
    url(r'^api/tasks/$', views.tasks_list),
]