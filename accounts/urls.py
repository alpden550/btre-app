from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.AccountLoginView.as_view(), name='login'),
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('logout/', views.AccountLogoutView.as_view(), name='logout'),
    path('dashboard/', views.AccountDashboardView.as_view(), name='dashboard'),
]
