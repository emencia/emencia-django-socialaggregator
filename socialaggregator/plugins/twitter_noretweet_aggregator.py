from datetime import datetime

from twitter_aggregator import Aggregator as TwitterAggregator


class Aggregator(TwitterAggregator):

    def search(self, query):
        res = self.connector.search.tweets(q=query)
        datas = []
        for tweet in res['statuses']:
            if 'retweeted_status' not in tweet:
                data = {'social_id': tweet['id_str'],
                        'name': 'tweet %s' % tweet['id_str'],
                        'slug': 'tweet_%s' % tweet['id_str'],
                        'language': tweet['lang'],
                        'ressource_date': datetime.strptime(tweet['created_at'],
                                                            self.datetime_format),
                        'description': tweet['text'],
                        'author': tweet['user']['name'],
                        }
                datas.append(data)
        return datas
