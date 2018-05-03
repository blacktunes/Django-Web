from django.conf.urls import url

from . import views

app_name = 'message_board'

urlpatterns = [
    url(r'^message_board/$', views.message_board, name='message_board'),

]

