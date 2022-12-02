from django.db import models
from django.contrib.auth.models import User


class CanvasPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    drawing = models.ImageField(upload_to='art')
    description = models.TextField(max_length=120, blank=True, null=True)
    