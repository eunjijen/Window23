# Generated by Django 4.1.7 on 2023-06-27 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0007_remove_idfinedust_place"),
    ]

    operations = [
        migrations.CreateModel(
            name="Emotion",
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
                ("emotion", models.BooleanField(default=True)),
            ],
        ),
    ]
