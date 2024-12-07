from django.core.exceptions import ValidationError


def game_platform_and_genre_name_validator(value):
    weird_characters_count = 0

    for char in value:
        if not char.isalnum():
            weird_characters_count += 1

    if len(value) == weird_characters_count:
        raise ValidationError("Please write the name using letters.")
    return value