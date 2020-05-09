from django.views.generic.base import TemplateView


class AccountRegisterView(TemplateView):
    """View to register a new account."""

    template_name = 'accounts/register.html'


class AccountDashboardView(TemplateView):
    """View to show an account dashboard."""

    template_name = 'accounts/dashboard.html'
