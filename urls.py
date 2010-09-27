from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('domains.views',
    (r'^$', 'view_homepage', {'homepage_template':'homepage.html'}, 'homepage'),
    (r'^check_status/$', 'view_check_status', {}, 'check_status'),
    (r'^check_all/$', 'view_check_all', {}, 'check_all'),
)