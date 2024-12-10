from django.contrib import admin
from games.models import Game, Review

# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_genre', 'get_platform', 'release_date',)

    def get_genre(self, obj):
        return ", ".join([genre.genre_name for genre in obj.genre.all()])

    get_genre.short_description = 'Genre'

    def get_platform(self, obj):
        return ', '.join([platform.platform_name for platform in obj.platform.all()])

    get_platform.short_description = 'Platform'
    search_fields = ('name', 'developer')
    ordering = ('-release_date', 'name')
    list_filter = ('release_date', 'genre', 'platform')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'rating', 'created_at')
    ordering = ('-created_at',)
    list_filter = ('created_at', 'user', 'game', 'rating')
    search_fields = ('user', 'game')


