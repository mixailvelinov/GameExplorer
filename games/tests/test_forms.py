from django.test import TestCase
from games.forms import GameReviewForm
from games.models import Game


class ReviewFormTest(TestCase):
    def test_create_review_with_valid_data_returns_True(self):
            valid_data = {
                'rating': 4,
                'review': 'This game is great but not perfect!'
            }

            form = GameReviewForm(data=valid_data)
            self.assertTrue(form.is_valid())

    def test_create_review_with_invalid_data__return_False(self):
        invalid_data = {
            'rating': 6,
            'review': 'This is a very good game!'
        }

        form = GameReviewForm(data=invalid_data)
        self.assertFalse(form.is_valid())

    def test_create_review_without_review_field__return_True(self):
        valid_data = {
            'rating': 5,
        }

        form = GameReviewForm(data=valid_data)
        self.assertTrue(form.is_valid())

