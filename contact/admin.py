from django.contrib import admin

# Register your models here.
from .models import Contact


class Contactadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contact, Contactadmin)
