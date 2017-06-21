from django.conf.urls import url

from . import views, api

app_name = 'app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clm_video$', views.clm_video, name='index'),
    url(r'^api/$', api.FacesList.as_view())

]
