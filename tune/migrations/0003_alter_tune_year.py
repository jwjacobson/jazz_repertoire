# Generated by Django 4.2.7 on 2023-11-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tune', '0002_alter_tune_options_alter_tune_composer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tune',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]