
from unicodedata import category
from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    MultiFieldPanel, 
    StreamFieldPanel, 
    InlinePanel
    )

from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from autoslug import AutoSlugField

from .article_pager import pager



class ArticlesListPage(MetadataPageMixin, Page):  
    max_count = 1    
    templates = 'Resource/articles_list_page.html'
    samples_per_page = models.IntegerField(null=True)


    content_panels = Page.content_panels + [
        MultiFieldPanel([
        
        FieldPanel('samples_per_page'),
        ], heading='No of Samples Per Page')
    ]

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)

        per_page = self.samples_per_page
        
        context = super().get_context(request, *args, **kwargs)
        all_posts = ArticleDetailPage.objects.live().public().order_by('-first_published_at')   
        
        context['articles'] =pager(request, all_posts, per_page=per_page)

       

        return context


class ArticleAuthor(models.Model):
    '''
    This is the blog authors model that will hold all the authors
    
    '''
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    author_bio = models.TextField(blank=True, null=True)  
   
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def post_author(self):
        fname = self.first_name
        lname = self.last_name
        lname = list(lname)
        initial = lname[0]
        
        return f'{fname} {initial}'

    class Meta:
        verbose_name = 'Article Author'
        verbose_name_plural = 'Article Authors'

register_snippet(ArticleAuthor)


class ArticleAuthorOrderable(Orderable):
    page = ParentalKey('resources.ArticleDetailPage', related_name='article_author')
    author = models.ForeignKey('resources.ArticleAuthor', on_delete=models.CASCADE)
    
    panels = [
        SnippetChooserPanel('author'),
    
    ]
class ArticleCategory(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'
        ordering = ['title',]

    panels = [
        FieldPanel('title'),
        
    ]

    def __str__(self):
        return self.title      


register_snippet(ArticleCategory)

class ArticleCategoryOrderable(Orderable):
    page = ParentalKey('resources.ArticleDetailPage', related_name='article_category')
    category = models.ForeignKey('resources.ArticleCategory', on_delete=models.SET_NULL, null=True, blank=True)
    
    panels = [
        SnippetChooserPanel('category'),
    
    ]

class ArticleTagPage(TaggedItemBase):
    content_object = ParentalKey('resources.ArticleDetailPage', related_name='article_tags', on_delete=models.CASCADE)


class ArticleDetailPage(MetadataPageMixin, Page):
    template = 'resources/article_detail_page.html'
    subpage_types =[]
    
    tags = ClusterTaggableManager(through=ArticleTagPage, blank=True)

    question_image = models.ForeignKey('wagtailimages.Image', blank=True, null=True, related_name='+', on_delete=models.SET_NULL) 

 
    sample_question = StreamField([
        ('sample_question', blocks.RichTextBlock()),
       
    ], max_num=1)
    
    sample_answer = StreamField([
        ('sample_answer', blocks.RichTextBlock()),
       
    ], max_num=1) 
   

    content_panels = Page.content_panels + [                  
        MultiFieldPanel([
            InlinePanel('article_author', label='Author', min_num=1, max_num=1)
        ], heading='Article Author'),

        MultiFieldPanel([
            InlinePanel('article_category', label='Category', min_num=1, max_num=1)
        ], heading='Article Category'),



        FieldPanel('tags'),

      
        ImageChooserPanel('question_image'),
        StreamFieldPanel('sample_question', ),
        StreamFieldPanel('sample_answer', ),
    ]    


    class Meta:
        verbose_name = 'Article Details'
        verbose_name_plural = 'Article Details'

