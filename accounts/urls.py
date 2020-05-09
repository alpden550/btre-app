from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('register/', views.AccountRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', views.AccountDashboardView.as_view(), name='dashboard'),
]
