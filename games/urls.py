from django.urls import path
from games import views

urlpatterns = [
    # Game Views
    path('', views.GamesListView.as_view(), name='games-list'),
    path('all-games/', views.AllGamesView.as_view(), name='all-games'),
    path('add/', views.AddGame.as_view(), name='add-game'),
    path('<slug:slug>/', views.GameDetailView.as_view(), name='games-detail'),
    path('<slug:slug>/edit/', views.EditGame.as_view(), name='edit-game'),
    path('<slug:slug>/review/', views.GameReview.as_view(), name='games-review'),
    path('<slug:slug>/review/<int:id>/edit', views.EditGameReview.as_view(), name='edit-review'),
    path('<slug:slug>/review/<int:id>/delete', views.DeleteGameReview.as_view(), name='delete-review'),
    path('<slug:slug>/all-reviews/', views.GameListAllReviews.as_view(), name='game-all-reviews'),

    # API
    path('api/<slug:slug>', views.ManageGameAPIView.as_view(), name='manage-games-api-view'),
    path('api/<slug:slug>/review/', views.ListAllGameReviewsAPIView.as_view(), name='list-all-game-reviews'),
    path('api/<slug:slug>/review/<int:id>/', views.ModifyReviewAPIView.as_view(), name='modify-review'),
]
