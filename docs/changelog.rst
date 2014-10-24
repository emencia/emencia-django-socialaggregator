.. _intro_changelog:

Changelog
=========

0.3.2
*****

* Fix dependancies in ``setup.py``;

0.3.2
*****

* Replace *django-filer* usage in profit of *django-filebrowser*;
* Replace previous migration (0016) to suit this change;

0.3
***

* Drop support for *DjangoCMS 2.x* and *Django<1.6* in profit of *DjangoCMS 3.x* and *Django>=1.6*;
* Use *django-filer* to manage image fields in models;
* Make the app menu in the cms toolbar;

0.2.9
*****

* Improved admin view for Feeds and Aggregators models;

0.2.8
*****

* Add in Ressource model some display options (``background_color`` and ``new_page``);

0.2.3
*****

* Add ``ressource_by_feed`` template tag to display ressources from specified feed without any pagination;
* Add ``EDSA_VIEW_TEMPLATE``, ``EDSA_TAG_TEMPLATE``, ``EDSA_PLUGIN_TEMPLATE`` settings and use them in view, tag and plugin;
* Some cleaning on the default template for views;

0.2.2
*****

* Add Sphinx documentation in ``docs/``;

0.2.1
*****

* Add new method on Ressource model to get unified content data;

0.2
***

* Add optional django-cms plugin to display feed ressources, little changes on default view template;

0.1.dev
*******

- Initial release. Alpha version
