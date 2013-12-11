from twitter import Twitter
from twitter import OAuth

from django.conf import settings
from generic import GenericAggregator


class TwitterAggregator(GenericAggregator):

    CONSUMER_KEY = settings.EDSA_TWITTER_CONSUMER_KEY
    CONSUMER_SECRET = settings.EDSA_TWITTER_CONSUMER_SECRET
    TOKEN = settings.EDSA_TWITTER_TOKEN
    SECRET = settings.EDSA_TWITTER_SECRET

    def init_connector(self):
        auth = OAuth(self.TOKEN, self.SECRET, self.CONSUMER_KEY,
                     self.CONSUMER_SECRET)
        self.connector = Twitter(auth=auth)

    def search(self, query):
        return self.connector.search.tweets(q=query)
