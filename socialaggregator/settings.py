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

EDSA_VIEW_TEMPLATE = 'socialaggregator/ressource_list.html'
EDSA_TAG_TEMPLATE = 'socialaggregator/ressource_list_tag.html'
EDSA_PLUGIN_TEMPLATE = 'socialaggregator/cms_plugin_feed.html'

# Image size limite (in Ko, 0 is no limit)
EDSA_RESSOURCE_IMAGE_SIZE = 0
