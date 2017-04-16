from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'v0/$', views.subjects),
    url(r'v0/stest$', views.static),
    url(r'v0/ntest$', views.newtemp),
    url(r'v0/test$', views.temp),
    url(r'v0/answer$', views.answer),
    url(r'v0/(?P<subj>\w+)/$', views.getsubject),
]