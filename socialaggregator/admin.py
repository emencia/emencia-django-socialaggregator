"""Admin for parrot.gallery"""
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from socialaggregator.models import Feed
from socialaggregator.models import Aggregator
from socialaggregator.models import Ressource


class FeedAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Feed, FeedAdmin)


class AggregatorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Aggregator, AggregatorAdmin)


class RessourceAdmin(admin.ModelAdmin):
    date_hierarchy = 'ressource_date'
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'author', 'language', 'social_type', 'query',
                    'ressource_date', 'activate')
    list_filter = ('social_type', 'activate',)
    ordering = ['-ressource_date', 'query']
admin.site.register(Ressource, RessourceAdmin)
