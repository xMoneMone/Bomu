from django.contrib import admin
from userprofile.models import UserProfile
from posts.admin import shorten


@admin.register(UserProfile)
class USerProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "nick", "bio_pv")

    def username(self, obj):
        username = str(obj.user)
        return shorten(username, 10)

    def nick(self, obj):
        return shorten(obj.nickname, 12)

    def bio_pv(self, obj):
        return shorten(obj.bio, 20)
