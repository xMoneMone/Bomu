from django.db import models
from django.contrib.auth.models import User
from userprofile.validators import validate_file_size


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='images', validators=(validate_file_size,), blank=True, null=True)
    nickname = models.CharField(max_length=12, blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True, null=True)

    def __str__(self):
        if self.nickname:
            return self.nickname
        return self.user
