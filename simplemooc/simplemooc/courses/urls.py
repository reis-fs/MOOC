from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.cursos, name='courses'),
    #url(r'^(?P<pk>\d+)/$', views.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
]
