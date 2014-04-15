"""Views for emencia-django-socialaggregator"""
from django.forms.models import model_to_dict
from django.views.generic import ListView
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.core import serializers
from django.conf import settings

from models import Ressource


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    response_class = HttpResponse

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        response_kwargs['content_type'] = 'application/json'
        return self.response_class(
            self.convert_context_to_json(context),
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return serializers.serialize("json", context)


class RessourceListView(JSONResponseMixin, ListView):
    """
    Display all ressources for all feeds
    """
    model = Ressource
    paginate_by = settings.EDSA_PAGINATION
    queryset = Ressource.activated.order_by('priority', '-ressource_date')
    template_name = settings.EDSA_VIEW_TEMPLATE
    
    def get_template_names(self):
        return [self.template_name]

    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        if self.request.GET.get('format', 'html') == 'json':
            context = context['ressource_list']
            return JSONResponseMixin.render_to_response(self, context)
        else:
            self.response_class = TemplateResponse
            return ListView.render_to_response(self, context)


class RessourceByFeedListView(RessourceListView):
    """
    Only display ressources from specified feed
    """
    def get_queryset(self):
        queryset = super(RessourceByFeedListView, self).get_queryset()
        slug = self.kwargs['slug']
        queryset = queryset.filter(feeds__slug=slug)
        return queryset
