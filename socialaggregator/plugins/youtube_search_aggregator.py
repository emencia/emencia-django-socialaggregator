from apiclient.discovery import build
from datetime import datetime

from django.conf import settings
try:
    from django.utils.text import slugify
except ImportError:
    # older django
    from django.template.defaultfilters import slugify
from generic import GenericAggregator


class Aggregator(GenericAggregator):

    DEVELOPER_KEY = settings.EDSA_GOOGLE_DEVELOPER_KEY
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    datetime_format = "%Y-%m-%dT%H:%M:%S.000Z"

    def init_connector(self):
        self.connector = build(self.YOUTUBE_API_SERVICE_NAME,
                               self.YOUTUBE_API_VERSION,
                               developerKey=self.DEVELOPER_KEY)

    def search(self, query):
        res = self.connector.search().list(q=query, part="id,snippet",
                                           maxResults=25, type="video",
                                           order="date").execute()
        datas = []
        for video in res['items']:
            infos = video['snippet']
            date = datetime.strptime(infos['publishedAt'],
                                     self.datetime_format)
            url = "http://www.youtube.com/watch?v=%s" % video['id']['videoId']
            data = {'social_id': video['id']['videoId'],
                    'name': infos['title'],
                    'slug': slugify(video['id']['videoId']+infos['title']),
                    'ressource_date': date,
                    'description': infos['description'],
                    'media_url': url,
                    'media_url_type': 'video',
                    'author': infos['channelTitle'],
                    }
            datas.append(data)

        return datas
