from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.AccountDashboardView.as_view(), name='dashboard'),
]
