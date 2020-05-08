from django.views.generic import ListView, TemplateView

from listings.models import Listing
from realtors.models import Realtor


class MainPageView(ListView):
    """View for main page."""

    model = Listing
    queryset = Listing.objects.select_related(
        'realtor',
    ).order_by(
        '-created_at',
    ).filter(
        is_published=True,
    )[:3]
    context_object_name = 'listings'
    template_name = 'pages/index.html'


class AboutPageView(TemplateView):
    """Class to manage about page."""

    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        """Add realtors and MVP realtors into context."""
        context = super().get_context_data(**kwargs)
        realtors = Realtor.objects.order_by('-hired_at')
        context['realtors'] = realtors
        context['mvp_realtors'] = realtors.filter(is_mvp=True)
        return context
