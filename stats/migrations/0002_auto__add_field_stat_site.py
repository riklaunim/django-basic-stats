# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Stat.site'
        db.add_column(u'stats_stat', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['sites.Site']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Stat.site'
        db.delete_column(u'stats_stat', 'site_id')


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
            'dpr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            's_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            's_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'w_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'w_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'stats.stat': {
            'Meta': {'object_name': 'Stat'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'referer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"})
        }
    }

    complete_apps = ['stats']