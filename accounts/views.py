from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from accounts.forms import RegisterForm


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


class AccountDashboardView(TemplateView):
    """View to show an account dashboard."""

    template_name = 'accounts/dashboard.html'
