# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table('moneyleft_entry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=10)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['moneyleft.Categories'])),
        ))
        db.send_create_signal('moneyleft', ['Entry'])

        # Adding model 'Categories'
        db.create_table('moneyleft_categories', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('moneyleft', ['Categories'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table('moneyleft_entry')

        # Deleting model 'Categories'
        db.delete_table('moneyleft_categories')


    models = {
        'moneyleft.categories': {
            'Meta': {'object_name': 'Categories'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'moneyleft.entry': {
            'Meta': {'object_name': 'Entry'},
            'amount': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '10'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['moneyleft.Categories']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['moneyleft']