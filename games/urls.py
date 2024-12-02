from django.urls import path, include

from games import views

urlpatterns = [
    path('', views.GamesListView.as_view(), name='games-list'),
    path('all-games', views.AllGamesView.as_view(), name='all-games'),
    path('<slug:slug>', views.GameDetailView.as_view(), name='games-detail'),
    path('<slug:slug>/review/', views.GameReview.as_view(), name='games-review'),
    path('<slug:slug>/all-reviews/', views.GameListAllReviews.as_view(), name='game-all-reviews'),

    #API
    path('api/', include([
        path('create-game/', views.GameCreateApiView.as_view(), name='create-game'),
        path('all-games/', views.GamesViewAPI.as_view(), name='games-view-api'),
        path('<slug:slug>/', include([
            path('edit/', views.UpdateExistingGame.as_view(), name='edit-game'),
            path('delete/', views.DeleteExistingGame.as_view(), name='delete-game'),
            path('review/', views.ListAllGameReviewsAPIView.as_view(), name='list-all-game-reviews'),
            path('review/<int:id>/', views.ModifyReviewAPIView.as_view(), name='modify-review')
        ]))


    ]
    ))
]