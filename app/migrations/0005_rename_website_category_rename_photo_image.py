# Generated by Django 4.0.6 on 2022-07-19 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_websiteimage_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Website',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Photo',
            new_name='Image',
        ),
    ]
