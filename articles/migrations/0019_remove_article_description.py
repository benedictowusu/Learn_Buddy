# Generated by Django 5.0.2 on 2024-04-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_alter_article_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='description',
        ),
    ]
