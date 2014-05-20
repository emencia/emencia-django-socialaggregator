"""
Settings sample for emencia-django-socialaggregator (EDSA)
"""
gettext = lambda s: s

# Twitter access keys
EDSA_TWITTER_TOKEN = 'FILLME'
EDSA_TWITTER_SECRET = 'FILLME'
EDSA_TWITTER_CONSUMER_KEY = 'FILLME'
EDSA_TWITTER_CONSUMER_SECRET = 'FILLME'

# Instagram access keys
EDSA_INSTAGRAM_ACCESS_TOKEN = 'FILLME'

# Facebook access keys
EDSA_FB_APP_ID = 'FILLME'
EDSA_FB_APP_SECRET = 'FILLME'
# Google+ access keys
EDSA_GOOGLE_DEVELOPER_KEY = 'FILLME'

# Pagination for ressource list in views
EDSA_PAGINATION = 16

# Enabled plugins and their engine
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

# Used templates
EDSA_VIEW_TEMPLATE = 'socialaggregator/ressource_list.html'
EDSA_TAG_TEMPLATE = 'socialaggregator/ressource_list_tag.html'
EDSA_PLUGIN_TEMPLATE = 'socialaggregator/cms_plugin_feed.html'

# Image size limit (in Ko, use 0 for no size limit)
EDSA_RESSOURCE_IMAGE_SIZE = 0

# Various ressource fields choices
EDSA_RESSOURCE_VIEW_SIZES = (
    ('default', gettext('default')),
    ('xsmall', gettext('Xsmall')),
    ('small', gettext('small')),
    ('medium', gettext('medium')),
    ('large', gettext('large')),
    ('xlarge', gettext('Xlarge')),
)

EDSA_RESSOURCE_TEXT_DISPLAY = (
    ('default', gettext('default')),
    ('bottom', gettext('bottom')),
    ('top', gettext('top')),
)

EDSA_RESSOURCE_BUTTON_COLOR = (
    ('white', gettext('white')),
    ('black', gettext('black')),
    ('primary', gettext('primary')),
    ('secondary', gettext('secondary')),
    ('tertiary', gettext('tertiary')),
)

EDSA_RESSOURCE_MEDIA_TYPE = (
    ('url', gettext('url')),
    ('image', gettext('image')),
    ('video', gettext('video')),
)

# Base media types to add to the ones from EDSA_PLUGINS
EDSA_RESSOURCE_BASE_MEDIA_TYPES = [
    ('edsa_article', 'Article'),
]