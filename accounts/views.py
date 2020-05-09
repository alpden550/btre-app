from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView


class AccountLoginView(LoginView):
    """Custom login view for accounts."""

    redirect_authenticated_user = True


class AccountRegisterView(TemplateView):
    """View to register a new account."""

    template_name = 'accounts/register.html'


class AccountDashboardView(TemplateView):
    """View to show an account dashboard."""

    template_name = 'accounts/dashboard.html'
