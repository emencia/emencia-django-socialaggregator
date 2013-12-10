"""Models for parrot.gallery"""
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager


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

    SOCIAL_PLUGINS = ((0, _('twitter')),
                      (1, _('instagram')),
                      (2, _('youtube')),)

    name = models.CharField(_('name'), max_length=250)
    query = models.CharField(_('query'), max_length=250)
    social_plugin = models.IntegerField(_('social plugin'),
                                        choices=FILETYPE_CHOICES)

    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)
    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    feeds = models.ManyToManyField(Feed, verbose_name=_('feeds'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('aggregator')
        verbose_name_plural = _('aggregators')


class Ressource(models.Model):
    """Model representing a ressource"""

    name = models.CharField(_('name'), max_length=250)

    description = models.TextField(_('description'), blank=True)
    short_description = models.TextField(_('short description'), blank=True)

    image = models.ImageField(_('image'), upload_to='social_aggregator',
                              blank=True)
    thumbnail = models.ImageField(_('thumbnail'),
                                  upload_to='social_aggregator/thumbs',
                                  blank=True)
    author = models.CharField(_('author'), max_length=250)
    ressource_date = models.DateTimeField(_('ressource date'))

    feeds = models.ManyToManyField(Feeds, verbose_name=_('feeds'))
    tags = TaggableManager()

    priority = models.IntegerField(
        _('display priority'), default=100,
        help_text=_('Set this value to 0 will hide the item'))

    creation_date = models.DateTimeField(_('creation date'), auto_now_add=True)

    slug = models.SlugField(_('slug'), unique=True, max_length=100)

    @models.permalink
    def get_absolute_url(self):
        return ('social_aggregator_ressource_detail', (self.slug,))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-priority', 'name')
        verbose_name = _('ressource')
        verbose_name_plural = _('ressources')
