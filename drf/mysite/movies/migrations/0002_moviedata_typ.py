# Generated by Django 4.2.8 on 2023-12-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="moviedata",
            name="typ",
            field=models.CharField(default="action", max_length=200),
        ),
    ]
