from django import template
from posts.models import CanvasLike

register = template.Library()


@register.filter(name='liked_by')
def check_relationship_exists(post, user):
    return CanvasLike.objects.filter(user=user, to_post=post).first()
