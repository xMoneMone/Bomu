from django.contrib import admin
from posts.models import CanvasComment, CanvasPost, CanvasLike


def shorten(string, val: int):
    if not string:
        return None
    if len(string) > val:
        return string[:val] + "..."
    else:
        return string


@admin.register(CanvasComment)
class CanvasCommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "comment_pv")

    def comment_pv(self, obj):
        comment = obj.comment
        return shorten(comment, 20)

    def post(self, obj):
        post = obj.to_post
        artist = str(post.user)
        return f"post #{post.id} by {shorten(artist, 10)}"

    def author(self, obj):
        author = str(obj.user)
        return shorten(author, 10)


@admin.register(CanvasPost)
class CanvasPostAdmin(admin.ModelAdmin):
    list_display = ("id", "artist", "description_pv", "likes")

    def artist(self, obj):
        return shorten(str(obj.user), 10)

    def likes(self, obj):
        result = CanvasLike.objects.filter(to_post=obj)
        return len(result)

    def description_pv(self, obj):
        return shorten(obj.description, 20)


@admin.register(CanvasLike)
class CanvasLikeAdmin(admin.ModelAdmin):
    list_display = ("id", "post")

    def post(self, obj):
        post = obj.to_post
        artist = str(post.user)
        return f"post #{post.id} by {shorten(artist, 10)}"
