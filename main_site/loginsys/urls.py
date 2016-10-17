from django.conf.urls import url
from . import views

# если хочешь передать как стори функции, то пиши '<appname>.views.<func_name>'
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
    url(r'^account/$', views.user_page, name="user_page"),
]
