from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suggestion/', views.GameSuggestionCreate.as_view(), name='suggestion_create'),
    path('platform/add/', views.CreatePlatform.as_view(), name='add-platform'),
    path('genre/add/', views.CreateGenre.as_view(), name='add-genre'),
    path('gamesuggestions/', views.GameSuggestionsList.as_view(), name='game-suggestions-list'),
    path('gamesuggestions/delete/<int:id>', views.delete_game_suggestion, name='game-suggestions-delete')
]

