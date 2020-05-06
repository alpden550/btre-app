from django.contrib import admin

from listings.models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'city', 'is_published', 'created_at')
    list_filter = ('city', 'state', 'zipcode')
    search_fields = ('title',)
    list_editable = ('is_published',)
