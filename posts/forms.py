from django import forms
from posts.models import CanvasPost, CanvasComment


class CanvasPostForm(forms.ModelForm):
    class Meta:
        model = CanvasPost
        fields = ['drawing', 'description']


class CanvasCommentForm(forms.ModelForm):
    class Meta:
        model = CanvasComment
        fields = ['comment']
