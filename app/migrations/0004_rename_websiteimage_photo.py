# Generated by Django 4.0.6 on 2022-07-19 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_website_thumbnail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WebsiteImage',
            new_name='Photo',
        ),
    ]
