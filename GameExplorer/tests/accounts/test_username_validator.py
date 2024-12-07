from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

User = get_user_model()


class TestUsername(TestCase):
    def test_create__user_with_username_3_letters_long__returns_True(self):
        user = User.objects.create(
            email='test@gmail.com',
            username='test',
            password='test12test'
        )

        user.full_clean()
        user.save()

        self.assertTrue(user)

    def test_create_user__with_username_less_than_3_letters__raises_validation_error(self):
        user = User.objects.create(
            email='test@gmail.com',
            username='t',
            password='test12test'
        )

        with self.assertRaises(ValidationError):
            user.full_clean()
            user.save()

