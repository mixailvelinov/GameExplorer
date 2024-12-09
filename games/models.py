from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError
from common.models import Platform, Genre
from common.validators import GamePlatformGenreNameValidator

# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=50, validators=[GamePlatformGenreNameValidator()], unique=True)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    platform = models.ManyToManyField(Platform)
    developer = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    game_cover = models.URLField()
    slug = models.SlugField(unique=True, blank=True)

    def clean(self):
        if Game.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            raise ValidationError({'slug': 'This slug is already taken. Please choose a different one.'})

        if not self.slug:
            self.slug = slugify(self.name)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Review(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    review = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
