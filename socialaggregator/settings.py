"""
Settings for emencia-django-socialaggregator (EDSA)
"""

EDSA_PLUGINS = {
    "edsa_twitter": {
        #"ENGINE": "socialaggregator.plugins.twitter_aggregator",
        "ENGINE": "socialaggregator.plugins.twitter_noretweet_aggregator",
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
    "edsa_wordpress_rss": {
        "ENGINE": "socialaggregator.plugins.wordpress_rss_aggregator",
        "NAME": "Wordpress RSS"
    },
    "edsa_youtube_search": {
        "ENGINE": "socialaggregator.plugins.youtube_search_aggregator",
        "NAME": "Youtube search"
    },
}

EDSA_PAGINATION = 20
