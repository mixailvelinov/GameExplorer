from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase


class AccountEditViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user', password='test_password', email='test_email@test.test')
        self.profile_url = reverse('account-edit', kwargs={'id': self.user.id})

    def test_editing_account_with_valid_data__should_redirect_to_account_details_page(self):
        self.client.login(username='test_email@test.test', password='test_password')
        redirect_url = reverse('account-details', kwargs={'id': self.user.id})

        data = {
            'first_name': 'Test',
            'last_name': 'Test'
        }

        response = self.client.post(self.profile_url, data)
        self.user.refresh_from_db()

        self.assertRedirects(response, redirect_url)
        self.assertEqual(self.user.profile.first_name, 'Test')
        self.assertEqual(self.user.profile.last_name, 'Test')

    def test_editing_account_first_name_and_last_name_starting_with_small_letter__changes_shouldnt_be_saved(self):
        self.client.login(username='test_email@test.test', password='test_password')

        data = {
            'first_name': 'test',
            'last_name': 'test'
        }

        response = self.client.post(self.profile_url, data)
        self.user.refresh_from_db()

        self.assertFalse(self.user.profile.first_name, 'test')
        self.assertFalse(self.user.profile.last_name, 'test')


