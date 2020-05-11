from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from accounts.forms import ContactForm
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


class ListingDetailView(FormMixin, DetailView):
    """Manage detail listing."""

    model = Listing
    queryset = Listing.objects.select_related('realtor')
    form_class = ContactForm
    context_object_name = 'listing'
    template_name = 'listings/listing.html'

    def get_success_url(self):
        """Return success url after form submitting."""
        return reverse('listings:listing', kwargs={'pk': self.object.pk})

    def get_initial(self):
        """Return the initial data to use for forms on this view."""
        initial = super().get_initial()
        user = self.request.user or None
        initial['listing'] = self.get_object().title
        if user:
            initial['name'] = user.first_name
            initial['email'] = user.email
        return initial

    def post(self, request, *args, **kwargs):
        """Save inquiry to db."""
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            contact = form.save(commit=False)
            contact.listing = self.object
            if user is not None:
                contact.user_id = user.id
            contact.save()
            messages.success(request, 'You request has been sent.')
            return super().form_valid(form)

        return super().form_invalid(form)


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
