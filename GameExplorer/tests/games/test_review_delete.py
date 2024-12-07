from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from common.models import Genre, Platform
from games.models import Game, Review

User = get_user_model()


class TestDeleteReview(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre_name='Test genre')
        self.platform = Platform.objects.create(platform_name='Test platform')

        self.game = Game.objects.create(
            name='Test Game',
            release_date='2024-12-07',
            developer='Test Dev',
            description='Test description',
            slug='test-slug'
        )

        self.game.genre.set([self.genre])
        self.game.platform.set([self.platform])

        self.user = User.objects.create_user(
            email='test@test.com',
            username='test',
            password='passwordtest'
        )

        self.other_user = User.objects.create_user(
            email='test2@test.com',
            username='test2',
            password='passwordtest2'
        )

        self.review = Review.objects.create(
            rating=5,
            user=self.user,
            game=self.game
        )

    def test_user_trying_to_delete_own_review__success(self):
        self.client.login(
            email='test@test.com',
            password='passwordtest'
        )

        response = self.client.post(
            reverse('delete-review', kwargs={'slug': self.game.slug, 'id': self.review.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('games-list'))
        self.assertFalse(Review.objects.filter(id=self.review.id).exists())



    def test_user_trying_to_delete_other_user_review__denied(self):
        self.client.login(
            email='test2@test.com',
            password='passwordtest2'
        )

        response = self.client.post(
            reverse('delete-review', kwargs={'slug': self.game.slug, 'id': self.review.id})
        )

        self.assertEqual(response.status_code, 403)
        self.assertTrue(Review.objects.filter(id=self.review.id).exists())


