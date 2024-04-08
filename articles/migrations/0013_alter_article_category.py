# Generated by Django 5.0.2 on 2024-04-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('FrontEnd', 'FrontEnd Development'), ('Backend', 'Backend Development')], default=1, max_length=50),
        ),
    ]
