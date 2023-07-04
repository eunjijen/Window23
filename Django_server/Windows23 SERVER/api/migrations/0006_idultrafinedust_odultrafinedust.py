# Generated by Django 4.1.7 on 2023-06-07 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_temp_rename_rain_rain_rainstatus"),
    ]

    operations = [
        migrations.CreateModel(
            name="IDUltraFineDust",
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
                ("value", models.FloatField()),
                ("date", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="ODUltraFineDust",
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
                ("value", models.FloatField()),
                ("date", models.DateTimeField()),
            ],
        ),
    ]
