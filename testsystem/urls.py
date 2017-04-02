from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hello$', views.preview, name='preview'),
    url(r'^get_test$', views.get_test, name='get_test'),
]