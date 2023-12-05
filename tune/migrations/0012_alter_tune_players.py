# Generated by Django 4.2.7 on 2023-11-29 22:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tune", "0011_remove_tune_players_tune_players"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tune",
            name="players",
            field=models.ManyToManyField(
                related_name="tunes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]