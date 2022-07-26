from django.contrib import admin

from menu.models import ThaiFoodWarm, ThaiFoodSalad, ThaiFoodDessert


class ThaiFoodWarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'composition', 'price', 'vegan', 'spicy', 'very_spicy')
    search_fields = ['name', 'composition']
    list_display


class ThaiFoodSaladAdmin(admin.ModelAdmin):
    list_display = ('name', 'composition', 'price', 'vegan', 'spicy', 'very_spicy')
    search_fields = ['name', 'composition']


class ThaiFoodDessertAdmin(admin.ModelAdmin):
    list_display = ('name', 'composition', 'price', 'vegan', 'spicy', 'very_spicy')
    search_fields = ['name', 'composition']

admin.site.register(ThaiFoodDessert, ThaiFoodDessertAdmin)
admin.site.register(ThaiFoodWarm, ThaiFoodWarmAdmin)
admin.site.register(ThaiFoodSalad, ThaiFoodSaladAdmin)


