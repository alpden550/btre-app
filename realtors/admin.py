from django.contrib import admin

from realtors.models import Realtor


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp', 'hired_at')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'is_mvp')
    list_editable = ('is_mvp',)
    search_fields = ('name',)
    list_per_page = 25
