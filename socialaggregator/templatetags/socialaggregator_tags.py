# -*- coding: utf-8 -*-
"""
Template tags
"""
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404

from socialaggregator.models import Ressource

register = template.Library()

@register.simple_tag(takes_context=True)
def ressource_by_feed(context, slug, template_name=settings.EDSA_TAG_TEMPLATE):
    """
    Display ressources from specified feed without any pagination
    
    * ``slug`` argument is a String containing the slug feed
    * ``template_name`` is a String containing the template path to use, default to ``settings.EDSA_TAG_TEMPLATE``
    """
    ressources = Ressource.activated.filter(feeds__slug=slug).order_by('priority', '-ressource_date')
    
    t = template.loader.get_template(template_name)
    context.update({
        'ressources': ressources,
    })
    content = t.render(template.Context(context))
    
    return mark_safe(content)
