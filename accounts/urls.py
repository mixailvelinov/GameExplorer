from accounts import views
from django.urls import path, include

urlpatterns = [
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),
    path('<int:id>/', include([
        path('', views.account_details, name='account-details'),
        path('edit/', views.AccountEditView.as_view(), name='account-edit'),
        path('delete/', views.account_delete, name='account-delete'),
        path('reviews/', views.AccountReviews.as_view(), name='account-reviews'),
    ]))
]

