import xadmin

from .models import *


class GameNameAdmin:
    list_display = ['name']
    search_fields = ['name']
    list_filter = []


class AboutAdmin:
    list_display = ['title', 'text']
    search_fields = ['title', 'text']
    list_filter = ['title']


class UpdateLogAdmin:
    list_display = ['date_added', 'text']
    search_fields = ['text']
    list_filter = ['date_added']


class TipAdmin:
    list_display = ['text']
    search_fields = ['text']
    list_filter = []


xadmin.site.register(GameName, GameNameAdmin)
xadmin.site.register(About, AboutAdmin)
xadmin.site.register(UpdateLog, UpdateLogAdmin)
xadmin.site.register(Tip, TipAdmin)
