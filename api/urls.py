from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'v0/$', views.subjects),
    url(r'v0/getinfosubject$', views.getinfosubject),
    url(r'v0/getinfostest$', views.getinfostest),
    url(r'v0/stest$', views.static),
    url(r'v0/check$', views.check),
]