# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_column('stats_mobile', 'dpr', 'device_pixel_ratio')
        db.rename_column('stats_mobile', 's_width', 'screen_width')
        db.rename_column('stats_mobile', 's_height', 'screen_height')
        db.rename_column('stats_mobile', 'w_height', 'window_height')
        db.rename_column('stats_mobile', 'w_width', 'window_width')

    def backwards(self, orm):
        pass

    models = {
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stats.mobile': {
            'Meta': {'object_name': 'Mobile'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'device_pixel_ratio': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'screen_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'screen_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'window_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'window_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'stats.stat': {
            'Meta': {'object_name': 'Stat'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'referer': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        }
    }

    complete_apps = ['stats']
