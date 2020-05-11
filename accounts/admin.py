from django.contrib import admin

from accounts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'name', 'phone', 'email', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('listing', 'name')
    list_filter = ('listing',)
