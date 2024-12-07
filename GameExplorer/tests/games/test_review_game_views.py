from django.contrib.auth import get_user_model
from django.urls import reverse

from common.models import Platform, Genre
from games.models import Game
from django.test import TestCase


class GameReviewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test_user', password='test_password', email='test_email@test.test')
        self.platform = Platform.objects.create(platform_name='Test Platform')
        self.genre = Genre.objects.create(genre_name='Test Genre')

        self.game = Game.objects.create(
            name='Test Game',
            release_date='2024-02-12',
            developer='Test Developer',
            description='Test Description',
            game_cover='http://example.com/game-cover.jpg'
        )

        self.game.genre.add(self.genre)
        self.game.platform.add(self.platform)
        self.game.save()

    def test_after_authenticated_user_creates_a_review__should_redirect_to_game_page(self):
        self.client.login(username='test_email@test.test', password='test_password')
        url = reverse('games-review', kwargs={'slug': self.game.slug})

        data = {
            'rating': 4,
            'review': 'This game is great but not perfect!'
        }

        response = self.client.post(url, data)

        self.assertRedirects(response, reverse('games-detail', kwargs={'slug': self.game.slug}))

    def test_if_not_authenticated_user_tries_to_create_review__should_redirect_to_login(self):
        url = reverse('games-review', kwargs={'slug': self.game.slug})
        data = {
            'rating': 5,
        }

        response = self.client.post(url, data)

        self.assertRedirects(response, '/accounts/login/?next=/games/test-game/review/')




