# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table(u'fx_app_article', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('snippet', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'fx_app', ['Article'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table(u'fx_app_article')


    models = {
        u'fx_app.article': {
            'Meta': {'object_name': 'Article'},
            'date': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'snippet': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['fx_app']