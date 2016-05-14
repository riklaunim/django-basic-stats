#!/usr/bin/python
import collections
from datetime import date
import urllib

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.sites.models import Site
from django.db.models import Q
from django.db.models import Count
from django.http import HttpResponse
from collections import OrderedDict
from django.views import generic

from stats.models import Stat, Mobile


class MobileDevicesStatistics(generic.TemplateView):
    template_name = 'stats/mobile_report.html'

    def get_context_data(self, **kwargs):
        context = super(MobileDevicesStatistics, self).get_context_data(**kwargs)
        context['distinct_user_agents_count'] = self._distinct_user_agents_count()
        context['total_entries'] = self._total_entries_stats()
        context['android_browsers'] = self._android_browsers_stats()
        context['android_devices'] = self._android_device_types()
        context['android_versions'] = self._android_versions()
        context['resolutions'] = self._popular_resolutions()
        return context

    def _distinct_user_agents_count(self):
        return Mobile.objects.all().values('user_agent').distinct().count()

    def _total_entries_stats(self):
        results = dict()
        results['all_entries'] = self._all_entries().count()
        results['ipad_entries'] = self._device_entries('ipad').count()
        results['ipod_entries'] = self._device_entries('ipod').count()
        results['iphone_entries'] = self._device_entries('iphone').count()
        results['android_entries'] = self._device_entries('android').count()
        results['s60_entries'] = self._device_entries('series 60').count()
        results['bada_entries'] = self._device_entries('bada').count()
        results['blackberry_entries'] = self._device_entries('blackberry').count()
        return results

    def _android_browsers_stats(self):
        results = dict()
        android = self._device_entries('android')
        results['opera'] = android.filter(user_agent__icontains='opera').count()
        results['webkit'] = android.filter(user_agent__icontains='applewebkit').count()
        results['firefox'] = android.filter(user_agent__icontains='firefox').count()
        return results

    def _popular_resolutions(self):
        all = self._all_entries()
        android = self._device_entries('android')
        all_resolutions = self._aggregate_queryset_by_resolution(all)
        android_resolution = self._aggregate_queryset_by_resolution(android)
        return {'android': android_resolution, 'all': all_resolutions}

    def _aggregate_queryset_by_resolution(self, queryset):
        return (queryset.values('screen_width', 'screen_height')
                .annotate(wcount=Count('screen_width'), hcount=Count('screen_height'))
                .order_by('-wcount')[:20])

    def _android_device_types(self):
        android = self._device_entries('android')
        all = android.count()
        phones = (android
                  .filter(Q(screen_width__lt=640, screen_height__lt=480) |
                          Q(screen_width__lt=480, screen_height__lt=640))
                  .count())
        tablets = all - phones
        return {'phones': phones, 'tablets': tablets}

    def _android_versions(self):
        result = OrderedDict()
        versions = ['android 2.1', 'android 2.2', 'android 2.3',
                    'android 4.0', 'android 4.1', 'android 4.2', 'android 4.3',
                    'android 4.4', 'android 5.0', 'android 5.1', 'android 6.0']
        for version in versions:
            result[version] = self._device_entries(version).count()
        return result

    def _device_entries(self, device):
        return self._all_entries().filter(user_agent__icontains=device)

    def _all_entries(self):
        return Mobile.objects

mobile_devices = staff_member_required(MobileDevicesStatistics.as_view())


class MobileDeviceLogger(generic.View):
    def get(self, request, **kwargs):
        self._save_device_hit(request)
        return HttpResponse('ok')

    def _save_device_hit(self, request):
        data = self._get_device_data(request.GET)
        meta = self._get_request_metadata(request.META)
        data['user_agent'] = meta['user_agent']
        if meta['ip'] and meta['user_agent']:
            Mobile.objects.get_or_create(ip=meta['ip'], date=date.today(), defaults=data)

    def _get_device_data(self, GET):
        data = dict()
        data['window_width'] = GET.get('window_width', None)
        data['window_height'] = GET.get('window_height', None)
        data['screen_width'] = GET.get('screen_width', None)
        data['screen_height'] = GET.get('screen_height', None)
        data['device_pixel_ratio'] = GET.get('device_pixel_ratio', '')
        return data

    def _get_request_metadata(self, META):
        meta = dict()
        meta['user_agent'] = META.get('HTTP_USER_AGENT', None)
        meta['ip'] = META.get('REMOTE_ADDR', None)
        return meta

log_mobile_device = MobileDeviceLogger.as_view()


class UniqueEntries(generic.TemplateView):
    template_name = 'stats/entries.html'

    def get_context_data(self, **kwargs):
        context = super(UniqueEntries, self).get_context_data(**kwargs)
        context['sites'] = Site.objects.all()
        context['daily_stats'] = self._get_daily_stats()
        return context

    def _get_daily_stats(self):
        return (Stat.objects
                .values('date')
                .annotate(hits=Count('date'))
                .order_by('-date'))

unique_entries = staff_member_required(UniqueEntries.as_view())


class LatestReferersList(generic.ListView):
    template_name = "stats/referers.html"

    def get_queryset(self):
        queryset = Stat.objects.order_by('-id').exclude(referer='')
        queryset = queryset.exclude(referer__icontains='google')
        queryset = queryset.exclude(referer__icontains='yahoo')
        queryset = queryset.exclude(referer__icontains='msn.com')
        queryset = queryset.exclude(referer__icontains='bing')
        queryset = queryset.exclude(referer__icontains='yandex')
        for site in Site.objects.all():
            queryset = queryset.exclude(referer__icontains=site.domain)
        return queryset.values_list('referer', flat=True)[:100]

last_referers = staff_member_required(LatestReferersList.as_view())


class GoogleSearchedKeywordsView(generic.TemplateView):
    template_name = "stats/google.html"

    def get_context_data(self, **kwargs):
        context = super(GoogleSearchedKeywordsView, self).get_context_data(**kwargs)
        context['keywords'] = list(self._get_google_keywords())
        return context

    def _get_google_keywords(self):
        referers = self._get_referers()
        keywords = self._get_keywords_from_urls(referers)
        return self._get_most_common_keywords(keywords)

    def _get_referers(self):
        return (Stat.objects.order_by('-id')
                .filter(referer__icontains='google')
                .values_list('referer', flat=True))

    def _get_keywords_from_urls(self, urls):
        for url in urls:
            url_parts = url.lower().split('q=')
            if len(url_parts) > 1:
                keyword = url_parts[1].split('&')[0]
                if keyword.strip():
                    yield urllib.unquote(keyword.encode('utf-8'))

    def _get_most_common_keywords(self, keywords):
        urls_collection = collections.Counter(keywords)
        return urls_collection.most_common(30)

google_search_keywords = staff_member_required(GoogleSearchedKeywordsView.as_view())


class StatsHomePage(generic.TemplateView):
    template_name = 'stats/home.html'

stats_home = staff_member_required(StatsHomePage.as_view())


@staff_member_required
def delete_all(request):
    Stat.objects.all().delete()
    return HttpResponse('ok')
