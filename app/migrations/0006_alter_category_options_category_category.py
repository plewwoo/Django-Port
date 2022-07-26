# Generated by Django 4.0.6 on 2022-07-19 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_website_category_rename_photo_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('website', 'Website'), ('graphic', 'Graphic'), ('photography', 'Photography')], default='website', max_length=100),
            preserve_default=False,
        ),
    ]
