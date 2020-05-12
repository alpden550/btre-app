from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from accounts.forms import RegisterForm
from accounts.models import Contact


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


class AccountDashboardView(LoginRequiredMixin, ListView):
    """View to show an account dashboard."""

    model = Contact
    context_object_name = 'contacts'
    login_url = reverse_lazy('accounts:login')
    template_name = 'accounts/dashboard.html'

    def get_queryset(self):
        """Get user's contacts."""
        return Contact.objects.select_related(
            'listing',
        ).filter(
            user_id=self.request.user.id,
        ).order_by('-created_at')

    def handle_no_permission(self):
        """Send error message if user is not authenticated."""
        messages.warning(self.request, 'You must be already loginned in.')
        return super().handle_no_permission()
