from django.contrib import admin
from posts.models import CanvasComment, CanvasPost, CanvasLike


class CanvasCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "to_post", "comment")


class CanvasPostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "description")


admin.site.register(CanvasComment, CanvasCommentAdmin)
admin.site.register(CanvasPost, CanvasPostAdmin)
admin.site.register(CanvasLike)
