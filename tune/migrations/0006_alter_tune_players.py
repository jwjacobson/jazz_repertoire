# Generated by Django 4.2.7 on 2023-11-29 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tune', '0005_tune_players'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tune',
            name='players',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tunes', to=settings.AUTH_USER_MODEL),
        ),
    ]
