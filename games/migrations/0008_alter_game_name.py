

import common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_alter_game_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=50, unique=True, validators=[common.validators.GamePlatformGenreNameValidator]),
        ),
    ]
