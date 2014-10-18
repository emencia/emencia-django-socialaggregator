"""Toolbar extensions for CMS"""
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


class SocialaggregatorToolbar(CMSToolbar):

    def populate(self):
        socialaggregator_menu = self.toolbar.get_or_create_menu(
            'socialaggregator-menu', _('SocialAggregator'))

        url = reverse('admin:socialaggregator_feed_add')
        socialaggregator_menu.add_sideframe_item(_('New feed'), url=url)

        url = reverse('admin:socialaggregator_ressource_add')
        socialaggregator_menu.add_sideframe_item(_('New ressource'), url=url)

        socialaggregator_menu.add_break()

        url = reverse('admin:socialaggregator_feed_changelist')
        socialaggregator_menu.add_sideframe_item(_('Feeds list'), url=url)

        url = reverse('admin:socialaggregator_ressource_changelist')
        socialaggregator_menu.add_sideframe_item(_('Ressources list'), url=url)


toolbar_pool.register(SocialaggregatorToolbar)
