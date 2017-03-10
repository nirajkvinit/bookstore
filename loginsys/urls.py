from django.conf.urls import url
from . import views

# если хочешь передать как стори функции, то пиши '<appname>.views.<func_name>'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^account/$', views.user_page, name="user_page"),
    url(r'^account/edit/$', views.edit_user_profile, name="user_profile_edit"),
]
