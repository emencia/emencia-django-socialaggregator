# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ressource.background_color'
        db.add_column(u'socialaggregator_ressource', 'background_color',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)

        # Adding field 'Ressource.new_page'
        db.add_column(u'socialaggregator_ressource', 'new_page',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ressource.background_color'
        db.delete_column(u'socialaggregator_ressource', 'background_color')

        # Deleting field 'Ressource.new_page'
        db.delete_column(u'socialaggregator_ressource', 'new_page')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 12, 0, 0)'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'favorite': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'feeds': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['socialaggregator.Feed']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
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
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'default': 'None'}),
            'updated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'view_size': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '100'})
        },
        u'taggit.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        },
        u'taggit.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_tagged_items'", 'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'taggit_taggeditem_items'", 'to': u"orm['taggit.Tag']"})
        }
    }

    complete_apps = ['socialaggregator']
