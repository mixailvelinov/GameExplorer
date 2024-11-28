from django.core.exceptions import ValidationError


def name_validator(value):
    if not value.isalpha():
        raise ValidationError('The name should contain only letters!')

    if not value[0].isupper():
        raise ValidationError('Name must start with a capital letter!')

    return value


def username_validator(value):
    if len(value) < 3:
        raise ValidationError('The username should have at least 3 characters!')

    return value


