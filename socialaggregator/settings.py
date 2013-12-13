"""
Settings for emencia-django-socialaggregator (EDSA)
"""

EDSA_PLUGINS = {
    "edsa_twitter": {
        "ENGINE": "socialaggregator.plugins.twitter_aggregator",
        "NAME": "Twitter"
    },
#    "edsa_instagram": {
#        "ENGINE": "socialaggregator.plugins.instagram",
#        "NAME": "Instagram"
#    },
#    "edsa_youtube": {
#        "ENGINE": "socialaggregator.plugins.youtube",
#        "NAME": "Youtube"
#    },
}
