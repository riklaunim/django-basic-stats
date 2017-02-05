# coding: utf-8
from django.utils import timezone
from django.contrib.sites.shortcuts import get_current_site

from stats.models import Stat


class StatsMiddleware(object):
    def process_request(self, request):
        today = timezone.now().date()
        ip = self._get_ip(request)
        entry = Stat.objects.filter(ip=ip, date=today)
        if not entry.exists():
            referer = self._get_referer(request)
            Stat.objects.create(ip=ip, referer=referer,
                                date=today,
                                site=get_current_site(request))

    def _get_referer(self, request):
        return request.META.get('HTTP_REFERER', '')

    def _get_ip(self, request):
        return request.META.get('REMOTE_ADDR', '127.0.0.0')
