from django.views.generic import ListView, TemplateView

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


class ListingDetailView(TemplateView):
    """Manage detail listing."""

    template_name = 'listings/listing.html'


class ListingSearchDetailView(TemplateView):
    """Manage listing's search."""

    template_name = 'listings/search.html'
