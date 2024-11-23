from accounts import views
from django.urls import path


urlpatterns = [
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
]