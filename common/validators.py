from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class GamePlatformGenreNameValidator:
    def __call__(self, value):
        weird_char_count = 0
        for char in value:
            if not char.isalnum():
                weird_char_count += 1

        if len(value) == weird_char_count:
            raise ValidationError('Please write the name using letters.')


# def game_platform_and_genre_name_validator(value):
#     weird_characters_count = 0
#
#     for char in value:
#         if not char.isalnum():
#             weird_characters_count += 1
#
#     if len(value) == weird_characters_count:
#         raise ValidationError("Please write the name using letters.")
#     return value
