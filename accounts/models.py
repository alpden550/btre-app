from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models import signals
from django.utils import timezone


class Contact(models.Model):
    """Object to represent inquiry fron contact."""

    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email', max_length=254)
    phone = models.CharField('Phone', max_length=50)
    message = models.TextField('Message', blank=True, null=True)
    created_at = models.DateTimeField('Created At', default=timezone.now, blank=True)
    user_id = models.IntegerField('User ID', null=True, blank=True)
    listing = models.ForeignKey(
        'listings.Listing',
        verbose_name='Listing',
        on_delete=models.CASCADE,
        related_name='contacts',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name


def send_email_inquiry(sender, instance, signal, *args, **kwargs):
    """Send email to manager about inquiring."""
    send_mail(
        'Property Listing Inquiry',
        f'There has been an inquiry for {instance.listing}\n\nSign into admin panel for more info.',  # noqa:E501
        settings.EMAIL_HOST_USER,
        [instance.listing.realtor.email],
    )


signals.post_save.connect(send_email_inquiry, sender=Contact)
