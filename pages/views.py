from django.views.generic import ListView, TemplateView

from listings.models import Listing


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
    template_name = 'pages/about.html'
