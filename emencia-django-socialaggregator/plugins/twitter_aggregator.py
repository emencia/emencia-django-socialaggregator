from twitter import Twitter
from twitter import OAuth

from django.conf import settings
from generic import GenericAggregator


class Aggregator(GenericAggregator):

    CONSUMER_KEY = settings.EDSA_TWITTER_CONSUMER_KEY
    CONSUMER_SECRET = settings.EDSA_TWITTER_CONSUMER_SECRET
    TOKEN = settings.EDSA_TWITTER_TOKEN
    SECRET = settings.EDSA_TWITTER_SECRET

    def init_connector(self):
        auth = OAuth(self.TOKEN, self.SECRET, self.CONSUMER_KEY,
                     self.CONSUMER_SECRET)
        self.connector = Twitter(auth=auth)

    def search(self, query):
        res = self.connector.search.tweets(q=query)
        datas = []
        for tweet in res['statuses']:
            data = {'social_id': tweet['id_str'],
                    'lang': tweet['lang'],
                    'creation_date': tweet['created_at'],
                    'description': tweet['text'],
                    'author': tweet['user']['name'],
                    }
            datas.append(data)

        return datas
