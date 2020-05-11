from django.db import models
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
    )

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.name
