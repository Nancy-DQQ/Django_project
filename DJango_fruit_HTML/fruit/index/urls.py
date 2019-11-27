from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^check_login$', views.check_login),
    url(r'^load_goods$', views.load_goods)

]
