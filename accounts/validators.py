from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError('The name should contain only letters!')

        if not value[0].isupper():
            raise ValidationError('Name must start with a capital letter!')


@deconstructible
class UsernameValidator:

    def __init__(self, min_length=3):
        self.min_length = min_length

    def __call__(self, value):
        spec_symbols_count = 0

        if len(value) < self.min_length:
            raise ValidationError(f'The username should have at least {self.min_length} characters!')

        for char in value:
            if not char.isalnum():
                spec_symbols_count += 1

            if spec_symbols_count == len(value):
                raise ValidationError("The username can't contain only special symbols.")

