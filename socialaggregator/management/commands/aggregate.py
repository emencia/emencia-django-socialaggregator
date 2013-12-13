from django.core.management.base import BaseCommand
from django.conf import settings
from socialaggregator.models import Aggregator, Ressource


def load_aggregators():
    """dynamical load all plugins aggregator"""
    plugins = {}
    for plugin, data in settings.EDSA_PLUGINS.items():
        mod = __import__(data['ENGINE'], globals(), locals(), ['Aggregator'],
                         -1)
        plugins[plugin] = mod.Aggregator()
    return plugins

AGGREGATORS = load_aggregators()


class Command(BaseCommand):

    # ici on peut mettre un message d'aide
    help = 'Aggregate socials feeds'

    # optionellement une aide pour les arguments
    args = 'social_type1, [social_type2], social_type3'

    def record_ressource(self, data, aggr):
        if not Ressource.objects.filter(social_id=data['social_id']).exists():
            rce = Ressource(**data)
            rce.social_type = aggr.social_plugin
            rce.query = aggr.query
            rce.save()
            for feed in aggr.feeds.all():
                rce.feeds.add(feed)

    def handle(self, *args, **options):
        if not args:
            # aggregate all data
            queryset = Aggregator.objects.all()
        else:
            # aggregate only specify data
            queryset = Aggregator.objects.filter(social_plugin__in=args)

        for aggr in queryset:
            plugin = AGGREGATORS[aggr.social_plugin]
            datas = plugin.search(aggr.query)
            for data in datas:
                self.record_ressource(data, aggr)
