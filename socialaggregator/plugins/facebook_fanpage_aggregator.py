from facebook import GraphAPI
from datetime import datetime

from django.conf import settings
from generic import GenericAggregator


class Aggregator(GenericAggregator):

    ACCESS_TOKEN = settings.EDSA_FB_FANPAGE_ACCESS_TOKEN

    datetime_format = "%Y-%m-%dT%H:%M:%S+0000"

    def init_connector(self):
        self.connector = GraphAPI(self.ACCESS_TOKEN)

    def search(self, query):
        res = self.connector.get_object("%s/posts" % query)
        datas = []
        for post in res['data']:
            if 'message' in post:
                if 'link' in post:
                    link = post['link']
                    media_url_type = 'url'
                else:
                    link = ""
                    media_url_type = ''
                date = datetime.strptime(post['created_time'],
                                         self.datetime_format)
                data = {'social_id': post['id'],
                        'name': 'fb fanpage %s' % post['id'],
                        'slug': 'fb_fanpage_%s' % post['id'],
                        'ressource_date': date,
                        'description': post['message'],
                        'media_url': link,
                        'media_url_type': media_url_type,
                        'author': post['from']['name'],
                        }
                datas.append(data)

        return datas
