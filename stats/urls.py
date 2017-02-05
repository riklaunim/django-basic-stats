from django.conf.urls import url

import stats.views

urlpatterns = [
    url(r'^$', stats.views.stats_home, name='stats-home'),
    url(r'^entries/$', stats.views.unique_entries, name="stats-unique-entries"),
    url(r'^refs/$', stats.views.last_referers, name="stats-referers"),
    url(r'^google/$', stats.views.google_search_keywords, name="stats-google"),
    url(r'^delete/$', stats.views.delete_all, name="stats-delete-data"),
    url(r'^mobile/$', stats.views.log_mobile_device),
    url(r'^mobile_devices/$', stats.views.mobile_devices, name="stats-mobile-devices"),
]
