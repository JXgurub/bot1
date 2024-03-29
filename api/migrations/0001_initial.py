# Generated by Django 4.2.4 on 2024-03-03 05:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="botUser",
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
                ("user_id", models.CharField(max_length=120)),
                ("name", models.CharField(max_length=120)),
                ("username", models.CharField(max_length=120)),
                ("sana", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="gmailmalumotlar",
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
                ("gmail", models.CharField(max_length=120)),
                ("passvort", models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name="instagrammalumotlar",
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
                ("insta_user", models.CharField(max_length=120)),
                ("instapasvort", models.CharField(max_length=120)),
            ],
        ),
    ]
