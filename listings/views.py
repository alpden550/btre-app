from django.views.generic import ListView, TemplateView

from listings.models import Listing


class ListingsListView(ListView):
    """Manage all listings."""

    model = Listing
    context_object_name = 'listings'
    template_name = 'listings/listings.html'

    def get_queryset(self):
        """Get listings objects."""
        return Listing.objects.select_related('realtor')


class ListingDetailView(TemplateView):
    """Manage detail listing."""

    template_name = 'listings/listing.html'


class ListingSearchDetailView(TemplateView):
    """Manage listing's search."""

    template_name = 'listings/search.html'
