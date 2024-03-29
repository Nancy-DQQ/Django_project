from django.conf.urls import url
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/v1/users
    url(r'^$', views.users),
    #http://127.0.0.1:8000/v1/users/<username>
    url(r'^/(?P<username>\w{1,11})$', views.users),
    #http://127.0.0.1:8000/v1/users/<username>/avatar
    url(r'^/(?P<username>\w{1,11})/avatar$', views.users_avatar),
    # http://127.0.0.1:8000/v1/users/weibo/url
    url(r'^/weibo/url$',views.users_weibo_url),
    # http://127.0.0.1:8000/v1/users/weibo/token
    url(r'^/weibo/token$',views.users_weibo_token)

]