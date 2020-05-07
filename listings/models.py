from django.conf import settings
from django.db import models


class Listing(models.Model):
    """Object to represent listing."""

    title = models.CharField('Title', max_length=200, unique=True, db_index=True)
    address = models.CharField('Listing Address', max_length=200)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50)
    zipcode = models.CharField('ZipCode', max_length=20)
    description = models.TextField('Description', blank=True)
    price = models.PositiveIntegerField('Price')
    bedrooms = models.PositiveIntegerField('BedRooms', default=1)
    bathrooms = models.DecimalField('BathRooms', max_digits=2, decimal_places=1, default=2)
    garage = models.PositiveIntegerField('Garage', default=0)
    square_feet = models.IntegerField('Square Feet', null=True, blank=True)
    lot_size = models.DecimalField(
        'Lot Size',
        max_digits=5,
        decimal_places=1,
        blank=True,
        null=True,
    )
    photo_main = models.ImageField('Main Photo', upload_to=settings.LISTING_PHOTO_PATH)
    photo1 = models.ImageField(upload_to=settings.LISTING_PHOTO_PATH, blank=True)
    photo2 = models.ImageField(upload_to=settings.LISTING_PHOTO_PATH, blank=True)
    photo3 = models.ImageField(upload_to=settings.LISTING_PHOTO_PATH, blank=True)
    photo4 = models.ImageField(upload_to=settings.LISTING_PHOTO_PATH, blank=True)
    photo5 = models.ImageField(upload_to=settings.LISTING_PHOTO_PATH, blank=True)
    photo6 = models.ImageField(upload_to=settings.LISTING_PHOTO_PATH, blank=True)
    is_published = models.BooleanField('Is Published', default=True)
    created_at = models.DateTimeField('Created At', auto_now_add=True)

    realtor = models.ForeignKey(
        'realtors.Realtor',
        verbose_name='Realtor',
        on_delete=models.DO_NOTHING,
        related_name='listings',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def __str__(self):
        return self.title
