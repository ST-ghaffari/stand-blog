# Generated by Django 5.0.6 on 2024-06-28 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_article_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]