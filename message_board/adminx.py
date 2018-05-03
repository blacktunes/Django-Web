import xadmin

from .models import *


class MessageBoardAdmin(object):
    list_display = ['text', 'name', 'created_time']
    search_fields = ['name', 'text']
    list_filter = ['name', 'created_time']


xadmin.site.register(MessageBoard, MessageBoardAdmin)
