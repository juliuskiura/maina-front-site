from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, MultiFieldPanel
from streams import nca_blocks
import requests
class HomePage(MetadataPageMixin, Page):
    max_count = 1
    
    templates = 'home/home_page.html'
    subpage_types = ['otherpages.AboutPage', 'resources.ArticlesListPage', 'otherpages.PolicyPage',]
    banner_title = models.CharField(max_length=43)
    banner_description = models.TextField()
    
    
    banner_cta = models.ForeignKey(
        'wagtailcore.page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'        
        )

    # section about
  
    section_about = StreamField([
        ('About_section', nca_blocks.EyebrowHeaderDescription(null=True))
    ],null=True, max_num=1)


    jumbo_area = StreamField([
        ('jumbo_cards', nca_blocks.JumboBlock(null=True))
    ],null=True, max_num=1)

    about_bullet = StreamField([
        ('about_bullet', blocks.CharBlock(required=False)),       
    ], null=True)

    section_about_content = StreamField([
         ('description', blocks.RichTextBlock(required=False, help_text='Section description'))        
        
    ], null=True, max_num=1)

    section_about_image= models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

 # section about
    core_features = StreamField([
        ('section_core_section', nca_blocks.EyebrowHeaderDescription()),
     
    ],null=True, max_num=1)

    core_features_cards = StreamField([        
        ('features_cards', nca_blocks.CardBlock())
    ],null=True, max_num=3)

# Citation Hub
    citation_hub = StreamField([
        ('citation_section', nca_blocks.EyebrowHeaderDescription()),        
    ],null=True, max_num=1)
    citation_styles = StreamField([
        ('citationStyle', nca_blocks.RichTextAndImage()),        
    ],null=True)
# timely updates
    timely_updates = StreamField([
        ('timely_updates', nca_blocks.EyebrowHeaderDescription()),        
    ],null=True, max_num=1)
    timely_updates_bullet = StreamField([
        ('updates_bullet', blocks.CharBlock(required=False)),       
    ], null=True)

# datasection
    datasection = StreamField([
        ('datasection_headings', nca_blocks.EyebrowHeaderDescription()),        
    ],null=True, max_num=1)
    data_card = StreamField([
        ('data_counter', nca_blocks.DataCardBlock()),        
    ],null=True)
  
    data_bullets = StreamField([
        ('data_bullets', blocks.CharBlock(required=False)),       
    ], null=True)



    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_description'),
        PageChooserPanel('banner_cta'),   

        StreamFieldPanel('jumbo_area'),    

        MultiFieldPanel(
        [ StreamFieldPanel('section_about'),
        StreamFieldPanel('about_bullet'),
        StreamFieldPanel('section_about_content'),
        ImageChooserPanel('section_about_image'),        
        ],
        heading="About Section",
        classname=""
        ),

        MultiFieldPanel(
        [
        
        StreamFieldPanel('core_features'),
        StreamFieldPanel('core_features_cards'),
        ],
        heading="Core Features Section",
        classname=""
        ),
        
        MultiFieldPanel(
        [
        StreamFieldPanel('citation_hub'),
        StreamFieldPanel('citation_styles'),

        ],
        heading="Citation Section",
        classname=""
        ),

        MultiFieldPanel(
        [
        StreamFieldPanel('timely_updates'),
        StreamFieldPanel('timely_updates_bullet'),

        ],
        heading="Timely CTA Updates Section",
        classname=""
        ),
        MultiFieldPanel(
        [
        StreamFieldPanel('datasection'),
        StreamFieldPanel('data_card'),
        StreamFieldPanel('data_bullets'),

        ],
        heading="Data Section",
        classname=""
        ),  
    ]



    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        try:
            managementUrl = 'https://appnursing.cannyva.com/assignments/getprice/'  
            pricingData = requests.get(managementUrl).json()
        
        except:
            pricingData ={}
    
        context['study_level'] = pricingData.get('study_level')
        context['service_category'] = pricingData.get('service_category')
        context['assignment_type'] = pricingData.get('assignment_type')
        context['turnaround'] = pricingData.get('turnaround')
   

        return context

