from django.urls import path

from games import views

urlpatterns = [
    path('', views.GamesListView.as_view(), name='games-list'),
    path('all-games', views.AllGamesView.as_view(), name='all-games'),
    path('<slug:slug>', views.GameDetailView.as_view(), name='games-detail'),
]