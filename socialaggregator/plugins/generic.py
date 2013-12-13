"""
generic class for aggregator plugin
"""


class GenericAggregator(object):

    connector = None

    def init_connector(self):
        pass

    def __init__(self):
        self.init_connector()

    def search(self, query):
        pass
