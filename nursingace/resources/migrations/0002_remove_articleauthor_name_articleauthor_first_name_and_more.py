# Generated by Django 4.0.4 on 2022-04-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleauthor',
            name='name',
        ),
        migrations.AddField(
            model_name='articleauthor',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articleauthor',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
