from datetime import date

from stats.models import Stat


class statsMiddleware(object):
    def process_request(self, request):
        today = date.today()
        ip = self._get_ip(request)
        entry = Stat.objects.filter(ip=ip, date=today)
        if not entry.exists():
            referer = self._get_referer(request)
            Stat.objects.create(ip=ip, referer=referer,
                                date=today,
                                site=request.current_site)

    def _get_referer(self, request):
        return request.META.get('HTTP_REFERER', '')

    def _get_ip(self, request):
        return request.META.get('REMOTE_ADDR', '127.0.0.0')
