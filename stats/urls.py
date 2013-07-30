from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns(
    'stats.views',
    url(r'^$', 'stats_home', name='stats-home'),
    url(r'^entries/$', 'unique_entries', name="unique-entries"),
    url(r'^refs/$', 'last_referers', name="referers"),
    url(r'^google/$', 'google_search_keywords', name="google"),
    url(r'^delete/$', 'delete_all', name="delete-stats-data"),
    url(r'^mobile/$', 'log_mobile_device'),
    url(r'^mobile_devices/$', 'mobile_devices', name="mobile-devices"),
)
