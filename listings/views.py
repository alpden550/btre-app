from django.views.generic import DetailView, ListView, TemplateView

from listings.choices import bedroom_choices, price_choices, state_choices
from listings.models import Listing


class ListingsListView(ListView):
    """Manage all listings."""

    model = Listing
    queryset = (
        Listing.objects.select_related(
            'realtor',
        ).order_by(
            '-created_at',
        ).filter(is_published=True)
    )
    context_object_name = 'listings'
    template_name = 'listings/listings.html'
    paginate_by = 6


class ListingDetailView(DetailView):
    """Manage detail listing."""

    model = Listing
    queryset = Listing.objects.select_related('realtor')
    context_object_name = 'listing'
    template_name = 'listings/listing.html'


class ListingSearchDetailView(TemplateView):
    """Manage listing's search."""

    template_name = 'listings/search.html'

    def get_context_data(self, **kwargs):
        """Pass listing choices into form."""
        context = super().get_context_data(**kwargs)
        context['bedroom_choices'] = bedroom_choices
        context['price_choices'] = price_choices
        context['state_choices'] = state_choices
        return context
