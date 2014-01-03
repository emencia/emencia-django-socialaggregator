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


def make_activated(modeladmin, request, queryset):
    queryset.update(activate=True)
make_activated.short_description = _("Mark selected ressources as activated")


def make_unactivated(modeladmin, request, queryset):
    queryset.update(activate=False)
make_unactivated.short_description = _("Mark selected ressources as \
                                        unactivated")


class RessourceAdmin(admin.ModelAdmin):
    date_hierarchy = 'ressource_date'
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'author', 'priority', 'view_size', 'language',
                    'social_type', 'query', 'ressource_date', 'activate',
                    'updated')
    list_editable = ('priority',)
    list_filter = ('social_type', 'activate', 'updated', 'feeds', 'language')
    ordering = ['updated', '-ressource_date', 'query']
    exclude = ('updated', 'update_date',)
    actions = [make_activated, make_unactivated]
    search_fields = ('name', 'author', 'description', 'short_description')
    fieldsets = ((_('Main infos'), {'fields': ('name', 'slug', 'description',
                                               'short_description', 'image',
                                               'thumbnail', 'media_url',
                                               'media_url_type')}),
                 (_('Extra infos'), {'fields': ('priority', 'activate',
                                                'author', 'language', 'feeds',
                                                'ressource_date', 'tags')}),
                 (_('Social network infos'), {'fields': ('social_id',
                                                         'social_type',
                                                         'query')}),
                 (_('Display infos'), {'fields': ('favorite', 'view_size',
                                                  'text_display',
                                                  'button_label',
                                                  'button_color')}))

admin.site.register(Ressource, RessourceAdmin)
