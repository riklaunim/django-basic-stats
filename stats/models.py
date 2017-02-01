from django.db import models


class Stat(models.Model):
    ip = models.GenericIPAddressField()
    referer = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    site = models.ForeignKey('sites.Site')

    class Meta:
        verbose_name = 'Stats'
        verbose_name_plural = 'Stats'

    def __unicode__(self):
        return self.referer


class Mobile(models.Model):
    ip = models.GenericIPAddressField()
    date = models.DateField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255)
    window_width = models.IntegerField(blank=True, null=True)
    window_height = models.IntegerField(blank=True, null=True)
    screen_width = models.IntegerField(blank=True, null=True)
    screen_height = models.IntegerField(blank=True, null=True)
    device_pixel_ratio = models.CharField(max_length=10, blank=True)

    class Meta:
        verbose_name = 'Mobile'
        verbose_name_plural = 'Mobile'

    def __unicode__(self):
        return self.user_agent
