from django import forms
from posts.models import CanvasPost


class CanvasPostForm(forms.ModelForm):
    class Meta:
        model = CanvasPost
        fields = ['bio']
        