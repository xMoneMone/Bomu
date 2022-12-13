from django.contrib import admin
from canvas.models import Palette


@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
