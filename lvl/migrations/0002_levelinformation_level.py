# Generated by Django 4.1.7 on 2023-06-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lvl", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="levelinformation",
            name="level",
            field=models.IntegerField(default=0),
        ),
    ]