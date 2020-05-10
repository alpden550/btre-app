from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from accounts.forms import RegisterForm


class AccountLoginView(SuccessMessageMixin, LoginView):
    """Custom login view."""

    success_message = '%(username)s successfully loginned in'
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class AccountLogoutView(LogoutView):
    """Custom logout view."""

    def dispatch(self, request, *args, **kwargs):
        """Add message about logout."""
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Successfully logged out.')
        return response


class AccountRegisterView(SuccessMessageMixin, CreateView):
    """View to register a new account."""

    template_name = 'accounts/register.html'
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
    success_message = '%(username)s was created successfully'

    def get(self, request, *args, **kwargs):
        """Redirect if user already loginned."""
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)


class AccountDashboardView(LoginRequiredMixin, TemplateView):
    """View to show an account dashboard."""

    login_url = reverse_lazy('accounts:login')
    permission_denied_message = 'You must be already loginned.'
    template_name = 'accounts/dashboard.html'

    def handle_no_permission(self):
        """Send error message if user is not authenticated."""
        messages.add_message(self.request, messages.WARNING, 'You must be loginned in')
        return super().handle_no_permission()
