# Generated by Django 5.0.4 on 2024-12-06 23:56

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_alter_gamesuggestion_game_suggestion_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(max_length=20, validators=[common.validators.game_platform_and_genre_name_validator]),
        ),
        migrations.AlterField(
            model_name='platform',
            name='platform_name',
            field=models.CharField(max_length=20, validators=[common.validators.game_platform_and_genre_name_validator]),
        ),
    ]
