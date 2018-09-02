from django.conf.urls import url

from . import views

app_name = 'message_board'

urlpatterns = [
    url(r'^message_board/$', views.message_board, name='message_board'),
    url(r'^message_board/api$', views.message_board_api, name='message_board_api'),
]

