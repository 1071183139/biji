from booktest import views
from django.conf.urls import url

urlpatterns=[
    url(r'^jingtai/$',views.jingtai),
    url(r'^$',views.index),
    url(r'^pic_upload/$', views.pic_upload),
    url(r'^pic_handle/$', views.pic_handle),
    url(r'^pic_show/$', views.pic_show),
    url(r'^csrf1/$', views.csrf1),
    url(r'^csrf2/$', views.csrf2),
]

