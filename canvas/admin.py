from django.contrib import admin
from canvas.models import Palette, ActivePalette


@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(ActivePalette)
class ActivePaletteAdmin(admin.ModelAdmin):
    list_display = ('id', 'palette')
