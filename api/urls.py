from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'v0/$', views.subjects),
    url(r'v0/stest$', views.static),
    url(r'v0/(?P<subj>\w+)/$', views.getsubject),
]