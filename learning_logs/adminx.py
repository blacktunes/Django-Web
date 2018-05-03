import xadmin

from .models import *


class TopicAdmin(object):
    list_display = ['text', 'owner', 'date_added']
    search_fields = ['text', 'owner']
    list_filter = ['owner', 'date_added']


class EntryAdmin(object):
    list_display = ['title', 'text', 'topic', 'owner', 'date_added']
    search_fields = ['title', 'topic', 'text']
    list_filter = ['topic', 'date_added']


xadmin.site.register(Topic, TopicAdmin)
xadmin.site.register(Entry, EntryAdmin)
