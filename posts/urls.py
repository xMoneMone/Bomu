from django.urls import path, include
from posts import views

urlpatterns = [
    path('<int:pk>', views.PostDetails.as_view(), name="post-details"),
    path('<int:pk>/edit', views.post_edit, name="post-edit"),
    path('<int:pk>/delete', views.post_delete, name="post-delete"),
    path('<int:pk>/like', views.post_like, name="post-like"),
    path('comment/<int:pk>/delete', views.comment_delete, name="comment-delete"),
    path('comment/<int:pk>/edit', views.comment_edit, name="comment-edit")
]
