from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey

from accounts.models import Account


class Platform(models.Model):
    platform_name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)


class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)


class GameSuggestion(models.Model):
    game_suggestion_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, null=True, blank=True)
    user = ForeignKey(Account, on_delete=models.CASCADE)