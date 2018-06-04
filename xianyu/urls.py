from django.conf.urls import include, url
# from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

import xadmin

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),
    url(r'', include('learning_logs.urls', namespace='learning_logs')),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^', include('message_board.urls', namespace='message_board')),
    url(r'^', include('introduce.urls', namespace='introduce')),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
