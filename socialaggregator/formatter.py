"""
Formatters for ressource datas
"""
class RessourceFormatterBase(object):
    """
    This is a dummy ressource formatter, its method "render" will simply return the 
    given instance, no format is applied here
    """
    def __init__(self, instance):
        self.instance = instance
    
    def render(self):
        return self.instance
    
class RessourceFormatterDefault(RessourceFormatterBase):
    """
    Default formatter, its goal is to unify various data types from social networks in 
    only one format to avoid to manage many various cases with all social networks
    
    This formatter is heavily linked to Foundation5 and private CSS that is not shipped 
    in the app, so you will have to implement it if needed
    """
    # CSS classes linked to size mode key name
    size_classes = {
        'small': 'grid-sizer2 h-sizer2',
        'medium': 'grid-sizer3 h-sizer1',
        'large': 'grid-sizer3 h-sizer2',
    }
    # CSS classes linked to social content type key name
    type_classes = {
        'edsa_facebook_fanpage': 'facebook',
        'edsa_twitter': 'twitter',
        'edsa_instagram': 'instagram',
        'edsa_article': 'article',
        'edsa_wordpress_rss': 'article',
        'edsa_pinterest': 'pinterest',
        'edsa_youtube': 'youtube',
        'edsa_youtube_search': 'youtube',
    }
    # CSS classes linked to social content type key name
    text_display_classes = {
        'default' : '',
        'top' : 'item-top',
        'bottom' : 'item-bottom',
    }
    
    def render(self):
        return {
            "id": self.instance.pk,
            "slug": self.instance.slug,
            "css_classes": self.get_css_classes(),
            "title": self.get_title(),
            "description": self.get_description(),
            "button": self.get_button(),
            "has_subblock": self.has_subblock(),
            "author": self.instance.author,
            "date": self.get_date(),
            "image": self.get_image(),
            "media": self.get_content_media(),
            "url": self.get_content_url(),
        }
    
    def has_subblock(self):
        return (self.instance.author or self.instance.ressource_date)
    
    def get_css_classes(self):
        css_classes = []
        if self.instance.view_size == 'default':
            css_classes.append(self.size_classes['medium'])
        else:
            css_classes.append(self.size_classes[self.instance.view_size])
        css_classes.append(self.get_type())
        css_classes.append(self.text_display_classes[self.instance.text_display])
        if self.get_content_url():
            css_classes.append("clickable")
        return " ".join(css_classes)
    
    def get_title(self):
        if self.get_type() in ('twitter', 'facebook', 'instagram'):
            return None
        return self.instance.name
    
    def get_description(self):
        return self.instance.description or self.instance.short_description
    
    def get_content_url(self):
        if self.instance.media_url and self.get_button() is None:
            return self.instance.media_url;
        return None
    
    def get_button(self):
        if self.instance.button_label and self.instance.media_url:
            return {
                'label': self.instance.button_label,
                'color': self.instance.button_color,
                'url': self.instance.media_url,
            }
        return None
    
    def get_type(self):
        return self.type_classes[self.instance.social_type]
    
    def get_author(self):
        if self.get_type() == 'youtube':
            return None
        return self.instance.author
    
    def get_content_media(self):
        if self.instance.media_url:
            return {
                'url': self.instance.media_url,
                'kind': self.instance.media_url_type,
            }
        return None
    
    def get_date(self):
        if self.get_type() == 'youtube':
            return None
        return self.instance.ressource_date
    
    def get_image(self):
        if self.instance.image:
            return self.instance.image.url
        return None
