from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Platform(models.Model):
    platform_name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)


class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
