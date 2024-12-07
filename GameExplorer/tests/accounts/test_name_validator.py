from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class TestNameValidator(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password', email='test_email@test.test')
        self.profile_url = reverse('account-edit', kwargs={'id': self.user.id})

    def test_editing_account_first_name_and_last_name_starting_with_small_letter__changes_not_be_saved(self):
        self.client.login(username='test_email@test.test', password='test_password')

        data = {
            'first_name': 'test',
            'last_name': 'test'
        }

        self.client.post(self.profile_url, data)
        self.user.refresh_from_db()

        self.assertFalse(self.user.profile.first_name, 'test')
        self.assertFalse(self.user.profile.last_name, 'test')


    def test_editing_account_first_name_as_digits__validation_error(self):
        self.client.login(username='test_email@test.test', password='test_password')

        data = {
            'first_name': '78'
        }

        self.client.post(self.profile_url, data)
        self.user.refresh_from_db()
        self.assertRaises(ValidationError)