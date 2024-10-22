# Generated by Django 4.1.7 on 2024-03-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URLSummary",
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
                ("url", models.URLField()),
                ("summary", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("intent", models.CharField(max_length=200)),
                ("executive_summary", models.TextField()),
                (
                    "urls_and_clean_summaries",
                    models.ManyToManyField(
                        related_name="urls_and_clean_summaries", to="myapp.urlsummary"
                    ),
                ),
                (
                    "urls_and_summaries",
                    models.ManyToManyField(
                        related_name="urls_and_summaries", to="myapp.urlsummary"
                    ),
                ),
            ],
        ),
    ]
