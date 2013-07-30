# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stat'
        db.create_table(u'stats_stat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('referer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'stats', ['Stat'])

        # Adding model 'Mobile'
        db.create_table(u'stats_mobile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('user_agent', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('w_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('w_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('s_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('s_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('dpr', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'stats', ['Mobile'])


    def backwards(self, orm):
        # Deleting model 'Stat'
        db.delete_table(u'stats_stat')

        # Deleting model 'Mobile'
        db.delete_table(u'stats_mobile')


    models = {
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
            'referer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stats']