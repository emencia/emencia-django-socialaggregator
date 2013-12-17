"""
Settings for emencia-django-socialaggregator (EDSA)
"""

EDSA_PLUGINS = {
    "edsa_twitter": {
        "ENGINE": "socialaggregator.plugins.twitter_aggregator",
        "NAME": "Twitter"
    },
    "edsa_instagram": {
        "ENGINE": "socialaggregator.plugins.instagram_aggregator",
        "NAME": "Instagram"
    },
    "edsa_facebook_fanpage": {
        "ENGINE": "socialaggregator.plugins.facebook_fanpage_aggregator",
        "NAME": "Facebook Fanpage"
    },
#    "edsa_youtube": {
#        "ENGINE": "socialaggregator.plugins.youtube",
#        "NAME": "Youtube"
#    },
}
