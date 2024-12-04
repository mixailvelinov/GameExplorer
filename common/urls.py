from django.urls import path, include

from common import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suggestion/', views.GameSuggestionCreate.as_view(), name='suggestion_create'),
    path('api/platform/', include([
])),

]