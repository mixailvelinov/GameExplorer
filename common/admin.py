from django.contrib import admin
from common.models import GameSuggestion, Platform, Genre


# Register your models here.


@admin.register(GameSuggestion)
class GameSuggestionAdmin(admin.ModelAdmin):
    fields = ['game_suggestion_name']
    list_display = ['game_suggestion_name', 'created_at']
    ordering = ['-created_at']
    search_fields = ['game_suggestion_name']


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    fields = ['platform_name']
    list_display = ['platform_name']
    ordering = ['platform_name']
    search_fields = ['platform_name']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ['genre_name']
    list_display = ['genre_name']
    ordering = ['genre_name']
    search_fields = ['genre_name']
