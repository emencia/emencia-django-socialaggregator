# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Changing field 'Ressource.image'
        db.alter_column(u'socialaggregator_ressource', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True))

        # Changing field 'Ressource.thumbnail'
        db.alter_column(u'socialaggregator_ressource', 'thumbnail', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True))

    def backwards(self, orm):
        # User chose to not deal with backwards NULL issues for 'Ressource.image'
        raise RuntimeError("Cannot reverse this migration. 'Ressource.image' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Ressource.image'
        db.alter_column(u'socialaggregator_ressource', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'Ressource.thumbnail'
        raise RuntimeError("Cannot reverse this migration. 'Ressource.thumbnail' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Ressource.thumbnail'
        db.alter_column(u'socialaggregator_ressource', 'thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'socialaggregator.aggregator': {
            'Meta': {'object_name': 'Aggregator'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feeds': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['socialaggregator.Feed']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'social_plugin': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'socialaggregator.feed': {
            'Meta': {'object_name': 'Feed'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'socialaggregator.ressource': {
            'Meta': {'ordering': "('-priority', 'name')", 'object_name': 'Ressource'},
            'activate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'background_color': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'button_color': ('django.db.models.fields.CharField', [], {'default': "'black'", 'max_length': '100'}),
            'button_label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 24, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'favorite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'feeds': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['socialaggregator.Feed']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'media_url': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'media_url_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'new_page': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'ressource_date': ('django.db.models.fields.DateTimeField', [], {}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'social_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'social_type': ('django.db.models.fields.CharField', [], {'default': "'edsa_article'", 'max_length': '250'}),
            'text_display': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '100'}),
            'thumbnail': ('filebrowser.fields.FileBrowseField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'updated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'view_size': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '100'})
        }
    }

    complete_apps = ['socialaggregator']