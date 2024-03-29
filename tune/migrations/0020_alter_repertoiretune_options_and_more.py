# Generated by Django 4.2.7 on 2023-12-14 14:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tune', '0019_alter_repertoiretune_knowledge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repertoiretune',
            options={'ordering': ['tune__title']},
        ),
        migrations.AlterUniqueTogether(
            name='repertoiretune',
            unique_together={('tune', 'player')},
        ),
    ]
