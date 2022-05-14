from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class EyebrowHeaderDescription(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, help_text='Section eyebrow')
    headline = blocks.CharBlock(required=False, help_text='Section headline')
    description = blocks.RichTextBlock(required=False, help_text='Section description')

    class Meta:
        template = 'streams/eyebrow_header_description.html'
        icon = 'edit'
        label = 'Section Eyebrow, Headling & Description'


class HeaderDescription(blocks.StructBlock):    
    headline = blocks.CharBlock(required=False, help_text='Section headline')
    description = blocks.RichTextBlock(required=False, help_text='Section description')

    class Meta:
        template = 'streams/eyebrow_header_description.html'
        icon = 'edit'
        label = 'Section Eyebrow, Headling & Description'

class CardBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ('fontawesome', blocks.CharBlock(required=False, help_text='Add Font awesome Markup reference')),
            ('headline', blocks.CharBlock(required=False, help_text='Card headline')),
            ('description', blocks.TextBlock(required=False, help_text='Section headline')),
            
        ])
    )
    class Meta:
        template = 'streams/feature-cards.html'
        icon = 'doc-full'

class JumboBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ('cardicon', ImageChooserBlock()),
            ('headline', blocks.CharBlock(required=False, help_text='Card headline')),
            ('description', blocks.TextBlock(required=False, help_text='Section headline')),
            
        ])
    )
    class Meta:
        template = 'streams/jumbo-cards.html'
        icon = 'doc-full'

class DataCardBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock([         
            ('max_count', blocks.CharBlock(required=False, help_text='Data Max number count')),
            ('item_text', blocks.CharBlock(required=False, help_text='Data item text below the counting numbers')),  
        ])
    )
    class Meta:
        template = 'streams/data-cards.html'
        icon = 'doc-full'
 
class RichTextAndImage(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False, help_text='Section eyebrow')
    headline = blocks.CharBlock(required=False, help_text='Section headline')
    description = blocks.RichTextBlock(required=False, help_text='Section description')
    image = ImageChooserBlock(required=False)

    class Meta:
        # template = 'streams/rich_text_and_image.html'
        icon = 'edit'
        label = 'Rich text with an image'
