from django.conf import settings
from django.db import models
from django.utils import timezone


class Realtor(models.Model):
    """Object to represent realtor."""

    name = models.CharField('Name', max_length=50)
    about = models.TextField('About', blank=True)
    photo = models.ImageField('Photo', upload_to=settings.UPLOAD_IMAGE_PATH, blank=True)
    phone = models.CharField('Phone', max_length=20)
    email = models.EmailField('Email', max_length=50, blank=True)
    is_mvp = models.BooleanField('Is MVP', default=False)
    hired_at = models.DateField('Hired At', default=timezone.now, blank=True)

    class Meta:
        verbose_name = 'Realtor'
        verbose_name_plural = 'Realtors'

    def __str__(self):
        return self.name
