from django.db import models
from canvas.validators import hex_code_validator


class Palette(models.Model):
    title = models.CharField(max_length=20, unique=True)
    c1 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c2 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c3 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c4 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c5 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c6 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c7 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c8 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c9 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c10 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c11 = models.CharField(max_length=7, validators=(hex_code_validator,))
    c12 = models.CharField(max_length=7, validators=(hex_code_validator,))


class ActivePalette(models.Model):
    palette = models.IntegerField()
