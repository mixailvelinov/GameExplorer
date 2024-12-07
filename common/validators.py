from django.core.exceptions import ValidationError

def game_platform_and_genre_name_validator(value):
    if not value.isalnum():
        raise ValidationError('Please use only words and letters for the game name.')
    return value