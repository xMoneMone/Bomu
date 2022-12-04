from django.urls import path, include
from posts import views

urlpatterns = [
    path('<pk>', views.post_details, name="post-details"),
    path('<pk>/edit', views.post_edit, name="post-edit"),
    path('<pk>/delete', views.post_delete, name="post-delete"),
    path('<pk>/like', views.post_like, name="post-like")
]
