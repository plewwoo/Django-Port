# Generated by Django 4.0.6 on 2022-07-19 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='thumbnail',
        ),
    ]
