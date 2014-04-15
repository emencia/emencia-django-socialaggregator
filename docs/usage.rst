.. _intro_usage:

*****
Usage
*****

As a view
---------

First, add this row in your ``urls.py`` : ::

    url(r'^socialaggregator/', include('socialaggregator.urls')),

Then you will access to your feed ressources list as a HTML page with an url like this : ::

    /socialaggregator/feed/sample/

Or you can use the JSON version : ::

    /socialaggregator/feed/sample/?format=json

Also there is a view to display **all** resssources from all feeds : ::

    /socialaggregator/

The default template use in these views comes from ``settings.EDSA_PLUGIN_TEMPLATE``.

As a templatetag
----------------

The tag syntax is the following : ::
    
    {% ressource_by_feed slug template_name %}

Where : 

* ``slug`` argument is a String containing the slug feed;
* ``template_name`` is a String containing the template path to use, default to ``settings.EDSA_TAG_TEMPLATE``;

So for example, load the templatetag and use the tag giving it the feed slug to use to list its ressources : ::

    {% load socialaggregator_tags %}

    <div class="row">
        {% ressource_by_feed 'parrot-apps-usa' %}
    </div>


As a django-cms plugin
----------------------

Just use the plugin named "Socialaggregator Feed Plugin" in your page with selecting the feed you want to list the ressources.

The default used template path comes from ``settings.EDSA_PLUGIN_TEMPLATE`` to display the feed ressources, change it in your project to use your own HTML layout.

Unified content datas
---------------------

Because feeds can contains ressources from many social networks, a method ``get_unified_render`` exist on the ``Ressource`` model. The method use formatter loaded from the setting ``RESSOURCE_FORMATTER`` if defined, else it will load the default formatter ``socialaggregator.formatter.RessourceFormatterDefault``.

The default formatter return a dict with an unified data scheme, so you can use it in your template without to test if a field is filled or not, etc.. This is optionnal, you can still directly use the ressource instance and play with its fields. You can use it like so : ::

    {% for ressource_item in feed_ressources %}{% with ressource_item.get_unified_render as ressource %}
    <li>
        {% if ressource.title %}<h2>{{ ressource.title }}</h2>{% endif %}
        {% if ressource.description %}<p>{{ ressource.description|safe|linebreaksbr }}</p>{% endif %}
    </li>
    {% endwith %}{% endfor %}

Note that the formatter is not automatically applied, so the JSON view output still return ressource instances serialized.
