from django.contrib import admin

from listings.models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'city', 'price', 'is_published', 'created_at', 'realtor')
    list_filter = ('realtor', 'city', 'state', 'zipcode')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_editable = ('is_published', 'realtor')
    list_per_page = 25
