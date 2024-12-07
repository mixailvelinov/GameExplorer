from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey

from accounts.models import Account
from common.validators import game_platform_and_genre_name_validator


class Platform(models.Model):
    platform_name = models.CharField(max_length=20, validators=[game_platform_and_genre_name_validator])
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.platform_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=20, validators=[game_platform_and_genre_name_validator])
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.genre_name


class GameSuggestion(models.Model):
    game_suggestion_name = models.CharField(max_length=30, validators=[game_platform_and_genre_name_validator])
    description = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.game_suggestion_name
