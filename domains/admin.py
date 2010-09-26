from django.contrib import admin
from domains.models import Domain

class DomainModelAdmin(admin.ModelAdmin):
    list_per_page = 25
    list_display = ('name', 'last_pinged')
    search_fields = ('name',)

admin.site.register(Domain, DomainModelAdmin)
