from django.views.generic import DetailView, ListView

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


class ListingSearchDetailView(ListView):
    """Manage listing's search."""

    model = Listing
    context_object_name = 'listings'
    template_name = 'listings/search.html'

    def get_context_data(self, **kwargs):
        """Pass listing choices into form."""
        context = super().get_context_data(**kwargs)

        context['bedroom_choices'] = bedroom_choices
        context['price_choices'] = price_choices
        context['state_choices'] = state_choices
        context['search_values'] = self.request.GET

        return context

    def get_queryset(self):
        """Queryset for listing search."""
        queryset = Listing.objects.order_by('-created_at')
        querystring = self.request.GET

        if querystring.get('keywords'):
            queryset = queryset.filter(description__icontains=querystring['keywords'])
        if querystring.get('city'):
            queryset = queryset.filter(city__iexact=querystring['city'])
        if querystring.get('state') and querystring.get('state') != 'State (All)':
            queryset = queryset.filter(state__iexact=querystring['state'])
        if querystring.get('bedrooms') and querystring.get('bedrooms') != 'Bedrooms (All)':
            queryset = queryset.filter(bedrooms__lte=querystring['bedrooms'])
        if querystring.get('price') and querystring.get('price') != 'Max Price (All)':
            queryset = queryset.filter(price__lte=querystring['price'])

        return queryset
