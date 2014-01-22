"""Models for parrot.gallery"""
from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.importlib import import_module

from taggit.managers import TaggableManager


def build_social_plugins_list():
    return [(plugin, datas["NAME"]) for plugin, datas in
            settings.EDSA_PLUGINS.items()]

SOCIAL_PLUGINS = build_social_plugins_list()


class Feed(models.Model):
    """Model for group ressource by feed"""

    name = models.CharField(_('name'), max_length=250)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('feed')
        verbose_name_plural = _('feeds')


class Aggregator(models.Model):
    """Model for an social feed aggregator"""

    name = models.CharField(_('name'), max_length=250)
    query = models.CharField(_('query'), max_length=250)
    social_plugin = models.CharField(_('social plugin'), max_length=250,
                                     choices=SOCIAL_PLUGINS)
    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)
    feeds = models.ManyToManyField(Feed, verbose_name=_('feeds'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('aggregator')
        verbose_name_plural = _('aggregators')


class RessourceQuerySet(models.query.QuerySet):
    def update(self, *args, **kwargs):
        kwargs['update_date'] = datetime.now()
        kwargs['updated'] = True
        super(RessourceQuerySet, self).update(*args, **kwargs)


class RessourceManager(models.Manager):
    def get_query_set(self):
        return RessourceQuerySet(self.model, using=self._db)


class ActivatedManager(RessourceManager):
    def get_query_set(self):
        queryset = super(ActivatedManager, self).get_query_set()
        return queryset.filter(activate=True)


class Ressource(models.Model):
    """Model representing a ressource"""

    VIEW_SIZES = (('default', _('default')),
                  ('xsmall', _('Xsmall')),
                  ('small', _('small')),
                  ('medium', _('medium')),
                  ('large', _('large')),
                  ('xlarge', _('Xlarge')),
                  )

    TEXT_DISPLAY = (('default', _('default')),
                    ('bottom', _('bottom')),
                    ('top', _('top')),
                    )

    BUTTON_COLOR = (('white', _('white')),
                    ('black', _('black')),
                    ('primary', _('primary')),
                    ('secondary', _('secondary')),
                    ('tertiary', _('tertiary')),
                    )

    MEDIA_TYPE = (('url', _('url')),
                  ('image', _('image')),
                  ('video', _('video')),
                  )

    SOCIAL_LIST = [('edsa_article', 'Article'), ] + SOCIAL_PLUGINS

    # ressource main infos
    name = models.CharField(_('name'), max_length=250)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)
    description = models.TextField(_('description'), blank=True)
    short_description = models.TextField(_('short description'), blank=True)
    image = models.ImageField(_('image'), upload_to='social_aggregator',
                              blank=True)
    thumbnail = models.ImageField(_('thumbnail'),
                                  upload_to='social_aggregator/thumbs',
                                  blank=True)
    media_url = models.URLField(_('media url'), blank=True, max_length=500)
    media_url_type = models.CharField(_('media url type'), max_length=100,
                                      blank=True, choices=MEDIA_TYPE)
    # extra infos
    priority = models.IntegerField(_('display priority'), default=100)
    activate = models.BooleanField(_('activate'), default=False)
    author = models.CharField(_('author'), max_length=250)
    language = models.CharField(_('language'), max_length=2, blank=True)
    feeds = models.ManyToManyField(Feed, verbose_name=_('feeds'))
    ressource_date = models.DateTimeField(_('ressource date'))
    tags = TaggableManager(blank=True)

    # social network info
    social_id = models.CharField(_('social_id'), max_length=250, blank=True)
    social_type = models.CharField(_('social plugin'), max_length=250,
                                   choices=SOCIAL_LIST,
                                   default="edsa_article")
    query = models.CharField(_('query'), max_length=250, blank=True)

    # display infos
    favorite = models.BooleanField(_('favorite'), default=False)
    view_size = models.CharField(_('view size'), max_length=100,
                                 choices=VIEW_SIZES, blank=False,
                                 default='default')
    text_display = models.CharField(_('text display'), max_length=100,
                                    choices=TEXT_DISPLAY, blank=False,
                                    default='default')
    button_label = models.CharField(_('button label'), max_length=100,
                                    blank=True)
    button_color = models.CharField(_('button color'), max_length=100,
                                    choices=BUTTON_COLOR, blank=False,
                                    default='black')

    # META DATA
    creation_date = models.DateTimeField(_('creation date'),
                                         default=datetime.now(),
                                         editable=False)
    update_date = models.DateTimeField(_('update date'),
                                       default=None)
    updated = models.BooleanField(_('updated'), default=False)

    # Managers
    objects = RessourceManager()
    activated = ActivatedManager()

    def save(self, *args, **kwargs):
        if self.update_date and not self.updated:
            self.updated = True
        self.update_date = datetime.now()
        super(Ressource, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('social_aggregator_ressource_detail', (self.slug,))

    def __unicode__(self):
        return self.name

    def get_unified_render(self):
        """
        Get the formatter for ressource datas then return the unified data render
        """
        formatter_path = getattr(settings, "RESSOURCE_FORMATTER", "socialaggregator.formatter.RessourceFormatterDefault")
        dot = formatter_path.rindex('.')
        module_name = formatter_path[:dot]
        class_name = formatter_path[dot + 1:] # Assume last item is the class to load
        try:
            _class = getattr(import_module(module_name), class_name)
        except ImportError:
            raise ImportError("'%s' cannot be imported from the setting 'RESSOURCE_FORMATTER'" % formatter_path)
        except AttributeError:
            raise AttributeError("'%s' cannot be imported from the setting 'RESSOURCE_FORMATTER'" % formatter_path)
        else:
            return _class(self).render()

    class Meta:
        ordering = ('-priority', 'name')
        verbose_name = _('ressource')
        verbose_name_plural = _('ressources')


# Optional plugin for DjangoCMS if installed
try:
    from cms.models import CMSPlugin
except ImportError:
    pass
else:
    class FeedPlugin(CMSPlugin):
        feed = models.ForeignKey('socialaggregator.Feed', related_name='plugins')

        def __unicode__(self):
            return self.feed.name