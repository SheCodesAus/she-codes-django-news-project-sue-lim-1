# Generated by Django 4.1.3 on 2022-12-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_newsstory_story_image_newsstory_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='content',
            field=models.TextField(verbose_name='Story'),
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date of Story'),
        ),
    ]
