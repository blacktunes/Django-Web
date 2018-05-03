from django.conf.urls import url

from . import views

app_name = 'introduce'

urlpatterns = [
    url(r'^update_log/$', views.update_log, name='update_log'),
    url(r'^about/$', views.about, name='about'),
    url(r'^tip/$', views.tip, name='tip'),

]
