from django.core.exceptions import ValidationError
from django.test import TestCase

from common.forms import GameSuggestionForm


class GameSuggestionFormTest(TestCase):

    def test_game_suggestion_form_with_valid_data__returns_True(self):
        valid_data = {
            'game_suggestion_name': 'Test Game',
            'description': 'Can you please add this game?'
        }

        form = GameSuggestionForm(data=valid_data)
        self.assertTrue(form, form.is_valid())

    def test_game_suggestion_form_with_long_game_name__return_error(self):
        invalid_data = {
            'game_suggestion_name': 'T' * 31,
            'description': 'Can you please add this game?'
        }

        form = GameSuggestionForm(data=invalid_data)
        self.assertIn('game_suggestion_name', form.errors)
        self.assertEqual(
            form.errors['game_suggestion_name'],
            ['Ensure this value has at most 30 characters (it has 31).']
        )

    def test_game_suggestion_form_with_invalid_game_name__return_error(self):
        invalid_data = {
            'game_suggestion_name': '____',
            'description': 'Can you please add this game?'
        }

        form = GameSuggestionForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            'Please use only words and letters for the game name.',
            form.errors['game_suggestion_name']
        )
