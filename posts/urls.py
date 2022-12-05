from django.urls import path, include
from posts import views

urlpatterns = [
    path('<pk>', views.PostDetails.as_view(), name="post-details"),
    path('<pk>/edit', views.post_edit, name="post-edit"),
    path('<pk>/delete', views.post_delete, name="post-delete"),
    path('<pk>/like', views.post_like, name="post-like"),
    path('<pk>/superlike', views.post_superlike, name="post-superlike"),
    path('comment/<pk>/delete', views.comment_delete, name="comment-delete"),
    path('comment/<pk>/edit', views.comment_edit, name="comment-edit")
]
