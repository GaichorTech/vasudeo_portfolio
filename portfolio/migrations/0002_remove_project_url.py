# Generated by Django 4.0 on 2022-01-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
    ]
