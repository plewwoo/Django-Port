# Generated by Django 4.0.6 on 2022-07-25 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_site_createdate_site_updatedate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Site',
            new_name='Work',
        ),
        migrations.AlterModelOptions(
            name='work',
            options={'verbose_name': 'Work', 'verbose_name_plural': 'Works'},
        ),
    ]
