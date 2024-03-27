# Generated by Django 5.0.2 on 2024-03-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('en', 'English'), ('ma', 'Maths'), ('hi', 'History')], max_length=50),
        ),
    ]
