emencia-django-social-aggregator
================================

This app is an aggregator of social network.

A command script will recover data from social network/external site from
**Aggregator** info that you specified into admin.It will stock them into
database, like **Ressource** and you could manage them into admin. You could
regroup **Ressource** by **Feed** and return them into JSON or HTML view.

Requires
********

* `django-taggit`_
* `twitter`_
* `python-instagram`_
* `facebook-sdk`_
* `feedparser`_
* `google-api-python-client`_


Install
*******

In your urls.py : ::

    url(r'^socialaggregator/', include('socialaggregator.urls')),

In your settings.INSTALLED_APPS : ::
   
    'taggit',
    'socialaggregator',
   
Then import basic settings in your settings file : ::

    from socialaggregator.settings import *

.. _django-taggit: https://pypi.python.org/pypi/django-taggit
.. _twitter: https://pypi.python.org/pypi/twitter
.. _python-instagram: https://pypi.python.org/pypi/python-instagram
.. _facebook-sdk: https://pypi.python.org/pypi/facebook-sdk
.. _feedparser: https://pypi.python.org/pypi/feedparser
.. _google-api-python-client: https://pypi.python.org/pypi/google-api-python-client

