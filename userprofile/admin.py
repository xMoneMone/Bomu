from django.contrib import admin
from userprofile.models import UserProfile
from posts.models import CanvasPost

admin.site.register(UserProfile)
admin.site.register(CanvasPost)
