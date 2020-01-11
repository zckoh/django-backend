from django.contrib import admin
from .models import CookingDish

class CookingDishAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_added')

admin.site.register(CookingDish, CookingDishAdmin)
