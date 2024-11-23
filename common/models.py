from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Review(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Platform(models.Model):
    platform_name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)


class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
