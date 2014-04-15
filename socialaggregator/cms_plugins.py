"""
Plugin controllers for Django-cms
"""
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from socialaggregator.models import FeedPlugin as FeedPluginModel
from socialaggregator.models import Ressource

class FeedPlugin(CMSPluginBase):
    """
    Simple plugin to display ressources from a Feed
    """
    model = FeedPluginModel # Model where data about this plugin is saved
    name = _("Socialaggregator Feed Plugin",) # Name of the plugin
    render_template = settings.EDSA_PLUGIN_TEMPLATE # template to render the plugin with
    
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'feed_instance': instance.feed,
            'feed_ressources': Ressource.activated.filter(feeds=instance.feed).order_by('priority', '-ressource_date'),
        })
        return context

plugin_pool.register_plugin(FeedPlugin) # register the plugin