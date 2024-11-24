from accounts import views
from django.urls import path


urlpatterns = [
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),
    path('<int:id>/', views.account_details, name='account-details'),
    path('<int:id>/edit/', views.AccountEditView.as_view(), name='account-edit'),
    path('<int:id>/delete/', views.account_delete, name='account-delete'),
]