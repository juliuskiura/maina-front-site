# Generated by Django 4.0.4 on 2022-04-21 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('otherpages', '0002_policy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Policy',
            new_name='PolicyPage',
        ),
    ]
