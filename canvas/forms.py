from django import forms
from canvas.models import Palette


class PaletteForm(forms.ModelForm):
    class Meta:
        model = Palette
        fields = '__all__'
        