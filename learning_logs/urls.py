from django.conf.urls import url

from . import views

app_name = 'learning_logs'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topics/$', views.topics, name='topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
        name='edit_entry'),
    url(r'^del_entry/(?P<entry_id>\d+)/$', views.del_entry,
        name='del_entry'),
    url(r'^new_entry2/(?P<topic_id>\d+)/$', views.new_entry2, name='new_entry2'),
    url(r'^edit_entry2/(?P<entry_id>\d+)/$', views.edit_entry2,
        name='edit_entry2'),
    url(r'^topic/api$', views.topic_api, name='topic_api'),
    url(r'^entry/api$', views.entry_api, name='entry_api'),
    url(r'^new_entry/api$', views.new_entry_api, name='new_entry_api'),
    url(r'^new_topic/api$', views.new_topic_api, name='new_topic_api')
]

