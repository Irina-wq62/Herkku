from django.contrib import admin
from .models import product


class productAdmin(admin.ModelAdmin):
    list_display = ("group", "name", "price","quantity")
    
admin.site.register(product, productAdmin)

