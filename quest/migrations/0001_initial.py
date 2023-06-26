# Generated by Django 4.1.7 on 2023-06-26 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Quest",
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
                ("title", models.CharField(max_length=50)),
                ("body", models.TextField(max_length=500)),
                ("quest_answer", models.SlugField()),
                ("xp", models.IntegerField()),
            ],
        ),
    ]
