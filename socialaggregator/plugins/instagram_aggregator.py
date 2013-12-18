from instagram.client import InstagramAPI
from datetime import datetime

from django.conf import settings
from generic import GenericAggregator


class Aggregator(GenericAggregator):

    ACCESS_TOKEN = settings.EDSA_INSTAGRAM_ACCESS_TOKEN

    def init_connector(self):
        self.connector = InstagramAPI(access_token=self.ACCESS_TOKEN)

    def search(self, query):
        if query.startswith('#'):
            query = query.lstrip('#')
        res = self.connector.tag_recent_media(tag_name=query)[0]
        datas = []
        for media in res:
            if media.caption:
                text = media.caption.text
            else:
                text = ""
            data = {'social_id': media.id,
                    'name': 'instagram %s' % media.id,
                    'slug': 'instagram_%s' % media.id,
                    'ressource_date': media.created_time,
                    'description': text,
                    'media_url': media.get_standard_resolution_url(),
                    'media_url_type': 'image',
                    'author': media.user.username,
                    }
            datas.append(data)

        return datas
