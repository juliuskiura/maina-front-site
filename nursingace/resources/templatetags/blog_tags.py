from django import template
from ..models import ArticleDetailPage
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags


register = template.Library()

@register.simple_tag
def total_posts():
    return ArticleDetailPage.objects.live().public().count() 
      

@register.inclusion_tag('resources/latest_posts.html')
def show_latest_posts(count=6):
    latest_posts = ArticleDetailPage.objects.live().public().order_by('-first_published_at')[:count]   
    return {'latest_posts': latest_posts}






@register.filter
def clean_block(value):
   
    try:
        plain_text = strip_tags(value)
    except:
        plain_text = 'Template error'
    
    return plain_text