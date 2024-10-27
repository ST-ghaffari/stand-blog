# Generated by Django 5.0.6 on 2024-07-11 10:12

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0019_alter_article_image_alter_article_pub_date"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ("-created",),
                "verbose_name": "نظر",
                "verbose_name_plural": "نظرات",
            },
        ),
        migrations.AlterField(
            model_name="article",
            name="pub_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 11, 10, 12, 25, 155620, tzinfo=datetime.timezone.utc
                ),
                verbose_name="تاریخ",
            ),
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="blog.article",
                        verbose_name="مقاله",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="کابر",
                    ),
                ),
            ],
            options={
                "verbose_name": "لایک",
                "verbose_name_plural": "لایک ها",
            },
        ),
    ]
