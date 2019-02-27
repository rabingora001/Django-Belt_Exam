from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^registration$', views.registration_process),
    url(r'^login$', views.login_process),
    url(r'^quotes$', views.quotes),
    url(r'^post_quote$', views.post_quote),
    url(r'^user/(?P<id>[0-9]+)$', views.user_page),
    # url(r'^myaccount/($', views.myaccount),
    url(r'^update$', views.update),
    # url(r'^post_likes$', views.post_likes),
    url(r'^log_off$', views.log_off),
]