# Generated by Django 5.0.2 on 2024-04-08 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_alter_article_description_alter_article_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='snippet',
            field=models.TextField(default=None, null=True),
        ),
    ]