from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'house_title', 'is_published', 'price', 'list_date', 'agent')
    list_display_links = ('id', 'house_title')
    list_filter = ('agent',)
    list_editable = ('is_published',)
    search_fields = ('house_title', 'description', 'address', 'school_campus', 'locality_name', 'house_type', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
