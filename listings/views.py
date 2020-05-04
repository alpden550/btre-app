from django.views.generic import TemplateView


class ListingsListView(TemplateView):
    """Manage all listings."""

    template_name = 'listings/listings.html'


class ListingDetailView(TemplateView):
    """Manage detail listing."""

    template_name = 'listings/listing.html'


class ListingSearchDetailView(TemplateView):
    """Manage listing's search."""

    template_name = 'listings/search.html'
