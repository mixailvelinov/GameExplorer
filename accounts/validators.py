from django.core.exceptions import ValidationError


def name_validator(value):
    if not value.isalpha():
        raise ValidationError('The name should contain only letters!')
    return value