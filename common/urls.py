from django.urls import path
from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suggestion/', views.GameSuggestionCreate.as_view(), name='suggestion_create'),
]

