from django.conf.urls import url

from . import views

app_name = 'introduce'

urlpatterns = [
    url(r'^updata_log/$', views.update_log, name='update_log'),
    url(r'^about/$', views.about, name='about'),
    url(r'^tip/$', views.tip, name='tip'),
    url(r'^about/api/$', views.about_api, name='about_api'),
    url(r'^gamename/api$', views.gamename_api, name='gamename_api'),
    url(r'^updata_log/api$', views.update_log_api, name='update_log_api'),
]
