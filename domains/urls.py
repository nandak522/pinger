from django.conf.urls.defaults import *
urlpatterns = patterns('domains.views',
    (r'^$', 'view_all_domains', {'all_domains_template':'domains.html'}, 'domains'),
    (r'^(?P<domain_id>\d+)/$', 'view_domain_profile', {'domain_profile_template':'domain_profile.html'}, 'domain_profile'),
)
