# Generated by Django 4.0.4 on 2022-04-18 05:56

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_homepage_core_features_cards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='core_features',
            field=wagtail.core.fields.StreamField([('section_core_section', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Section eyebrow', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Section headline', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Section description', required=False))])), ('features_cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('fontawesome', wagtail.core.blocks.CharBlock(help_text='Add Font awesome Markup reference', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Card headline', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Section headline', required=False))])))]))], null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_about',
            field=wagtail.core.fields.StreamField([('About_section', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Section eyebrow', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Section headline', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Section description', required=False))], null=True))], null=True),
        ),
    ]
