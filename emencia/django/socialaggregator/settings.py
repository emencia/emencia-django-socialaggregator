"""
Settings for emencia.django.socialaggregator (EDSA)
"""

EDSA_PLUGINS = {
    "edsa_twitter": {
        "ENGINE": "emencia.django.socialaggregator.plugins.twitter_aggregator",
        "NAME": "Twitter"
    },
    "edsa_instagram": {
        "ENGINE": "emencia.django.socialaggregator.plugins.instagram",
        "NAME": "Instagram"
    },
    "edsa_youtube": {
        "ENGINE": "emencia.django.socialaggregator.plugins.youtube",
        "NAME": "Youtube"
    },
}
