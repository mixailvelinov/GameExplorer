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

    def test_game_suggestion_form_with_invalid_game_name__return_False(self):
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

