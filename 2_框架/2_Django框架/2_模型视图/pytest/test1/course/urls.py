from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^set_cookie/$',views.set_cookie),
    url(r'^get_cookie/$',views.get_cookie),

    url(r'^set_session/$',views.set_session),
    url(r'^get_session/$',views.get_session),

    url(r'^json1/$', views.json1),
    url(r'^json2/$', views.json2),

    # url(r'^\d+/$',views.show1),
    url(r'^(\d+)/$',views.show1),
    url(r'^(?P<id1>\d+)/$',views.show1),

    url(r'^method1/$', views.method1),
    url(r'^method2/$', views.method2),
    url(r'^method3/$', views.method3),

    url(r'^get1/$',views.get1),
    url(r'^get2/$',views.get2),
    url(r'^get3/$',views.get3),


    url(r'^post1/$',views.post1),
    url(r'^post2/$',views.post2),

    url(r'^fan1/$', views.fan1),

    url(r'^fan2/$', views.fan2),
    url(r'^fan_show/$', views.fan2,name='fan3'),
]