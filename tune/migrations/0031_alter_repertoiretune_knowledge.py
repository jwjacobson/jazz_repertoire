# Generated by Django 4.2.7 on 2024-01-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tune", "0030_remove_tune_is_ballad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="repertoiretune",
            name="knowledge",
            field=models.CharField(
                choices=[("know", "know"), ("learning", "learning"), ("don't know", "don't know")],
                default="know",
                max_length=15,
            ),
        ),
    ]
