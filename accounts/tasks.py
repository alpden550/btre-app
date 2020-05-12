from django.conf import settings
from django.core.mail import send_mail

from btre.celery import app
from listings.models import Listing


@app.task
def send_email_inquiry(listing_id):
    """Send email to manager about inquiring."""
    listing = Listing.objects.get(pk=listing_id)
    send_mail(
        'Property Listing Inquiry',
        f'There has been an inquiry for {listing}\n\nSign into admin panel for more info.',  # noqa:E501
        settings.EMAIL_HOST_USER,
        [listing.realtor.email],
    )
