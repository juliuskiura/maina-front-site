# Generated by Django 4.0.4 on 2022-04-18 20:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_homepage_citation_styles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='citation_styles',
            field=wagtail.core.fields.StreamField([('citationStyle', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Section eyebrow', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Section headline', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Section description', required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))]))], null=True),
        ),
    ]