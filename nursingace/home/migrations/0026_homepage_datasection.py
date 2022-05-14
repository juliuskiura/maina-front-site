# Generated by Django 4.0.4 on 2022-04-20 06:18

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_homepage_timely_updates_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='datasection',
            field=wagtail.core.fields.StreamField([('timely_updates', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Section eyebrow', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Section headline', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Section description', required=False))]))], null=True),
        ),
    ]