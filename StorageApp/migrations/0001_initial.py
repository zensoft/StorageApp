# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GroupModel'
        db.create_table(u'StorageApp_groupmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descriptions', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('descriptions_test', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'StorageApp', ['GroupModel'])


    def backwards(self, orm):
        # Deleting model 'GroupModel'
        db.delete_table(u'StorageApp_groupmodel')


    models = {
        u'StorageApp.groupmodel': {
            'Meta': {'object_name': 'GroupModel'},
            'descriptions': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'descriptions_test': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['StorageApp']