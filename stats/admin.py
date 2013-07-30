from django.contrib import admin

from stats.models import *


class MobileAdmin(admin.ModelAdmin):
    list_display = ('user_agent', 'screen_width', 'screen_height', 'device_pixel_ratio')
    search_fields = ['user_agent']

admin.site.register(Mobile, MobileAdmin)
