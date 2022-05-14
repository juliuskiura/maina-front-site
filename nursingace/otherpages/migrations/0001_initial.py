# Generated by Django 4.0.4 on 2022-04-20 09:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0066_collection_management_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('section_about', wagtail.core.fields.StreamField([('About_section', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Section eyebrow', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Section headline', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Section description', required=False))], null=True))], null=True)),
                ('core_values', wagtail.core.fields.StreamField([('section_core_section', wagtail.core.blocks.StructBlock([('eyebrow', wagtail.core.blocks.CharBlock(help_text='Section eyebrow', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Section headline', required=False)), ('description', wagtail.core.blocks.RichTextBlock(help_text='Section description', required=False))]))], null=True)),
                ('core_values_cards', wagtail.core.fields.StreamField([('values_cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('fontawesome', wagtail.core.blocks.CharBlock(help_text='Add Font awesome Markup reference', required=False)), ('headline', wagtail.core.blocks.CharBlock(help_text='Card headline', required=False)), ('description', wagtail.core.blocks.TextBlock(help_text='Section headline', required=False))])))]))], null=True)),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Search image')),
                ('section_about_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]