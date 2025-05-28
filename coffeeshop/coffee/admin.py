from django.contrib import admin
from .models import Coffee

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name','price','qty')

admin.site.register(Coffee, CoffeeAdmin)