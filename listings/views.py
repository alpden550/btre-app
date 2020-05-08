from django.views.generic import DetailView, ListView, TemplateView

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
