from django.urls import path, include

from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suggestion/', views.GameSuggestionCreate.as_view(), name='suggestion_create'),
    path('api/platform/', include([
        path('', views.AllPlatformsAPIView.as_view(), name='all_platforms'),
        path('create/', views.CreatePlatformAPIView.as_view(), name='create_platform'),
        path('<int:id>/', views.ManagePlatformAPIView.as_view(), name='manage_platforms'),
])),


    #API
    path('api/genre/', include([
        path('', views.AllGenresAPIView.as_view(), name='all_genres'),
        path('create/', views.CreateGenreAPIView.as_view(), name='create_genre'),
        path('<int:id>/', views.ManageGenreAPIView.as_view(), name='manage_genre'),
    ]))
]