# Generated by Django 5.0.6 on 2024-07-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0009_contactus_alter_comment_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactus",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="title",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
