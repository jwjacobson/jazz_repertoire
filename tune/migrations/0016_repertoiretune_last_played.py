# Generated by Django 4.2.7 on 2023-12-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tune", "0015_rename_tune_repertoiretune_rep_tune"),
    ]

    operations = [
        migrations.AddField(
            model_name="repertoiretune",
            name="last_played",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
