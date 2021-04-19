from django.contrib import admin
from .models import PromoCode

class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'start_date', 'expiry_date', 'discount', 'active']
    list_filter = ['active', 'start_date', 'expiry_date']
    search_fields = ['code']

admin.site.register(PromoCode, PromoCodeAdmin)
