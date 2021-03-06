# Generated by Django 4.0.4 on 2022-04-20 00:32

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_homepage_citation_styles'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='timely_updates',
            field=wagtail.core.fields.StreamField([('citation_section', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Section eyebrow', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Section headline', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Section description', required=False))]))], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='timely_updates_bullet',
            field=wagtail.core.fields.StreamField([('about_bullet', wagtail.core.blocks.CharBlock(required=False))], null=True),
        ),
    ]
