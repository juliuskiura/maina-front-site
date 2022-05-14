from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.edit_handlers import StreamFieldPanel, MultiFieldPanel
from streams import nca_blocks
from home.models import HomePage


class AboutPage(MetadataPageMixin, Page):

    
   
    max_count = 1    
    templates = 'home/about_page.html'
    subpage_types = [] 
    section_about = StreamField([
        ('About_section', nca_blocks.EyebrowHeaderDescription(null=True))
    ],null=True, max_num=1)

    section_about_image= models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

 # section about
    core_values = StreamField([
        ('section_core_section', nca_blocks.EyebrowHeaderDescription()),
     
    ],null=True, max_num=1)

    core_values_cards = StreamField([        
        ('values_cards', nca_blocks.CardBlock())
    ],null=True, max_num=3)



    content_panels = Page.content_panels + [   

        MultiFieldPanel(
        [ StreamFieldPanel('section_about'),       
        ImageChooserPanel('section_about_image'),        
        ],
        heading="About Section",
        classname=""
        ),

        MultiFieldPanel(
        [
        StreamFieldPanel('core_values'),
        StreamFieldPanel('core_values_cards'),
        ],
        heading="Core Values Section",
        classname=""
        )       
      
    ]



    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        
        context['datasection'] =  HomePage.objects.all()[0].datasection
        context['data_card'] =  HomePage.objects.all()[0].data_card
        context['data_bullets'] =  HomePage.objects.all()[0].data_bullets

        return context



class PolicyPage(MetadataPageMixin, Page):
    subpage_types = []
    template = 'otherpages/policy.html'

    policy_body = StreamField([    
        ('policy_body', blocks.RichTextBlock()),     
    ])

    content_panels = Page.content_panels + [   
        StreamFieldPanel('policy_body')     
            
    ]

