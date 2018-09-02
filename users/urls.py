from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'users'

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'},
        name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^api', views.user_api, name='user_api'),
    url(r'^last_login/api', views.last_login_api, name='last_login_api')
]