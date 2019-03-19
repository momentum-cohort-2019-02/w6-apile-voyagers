from django.contrib import admin
from core.models import Site

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ('site_name')
