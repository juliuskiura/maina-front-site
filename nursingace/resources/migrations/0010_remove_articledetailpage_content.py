# Generated by Django 4.0.4 on 2022-04-20 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0009_alter_articledetailpage_sample_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articledetailpage',
            name='content',
        ),
    ]
