from django.db import models
from django.utils.text import slugify

from common.models import Platform, Genre


# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    platform = models.ManyToManyField(Platform)
    developer = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    game_cover = models.URLField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


