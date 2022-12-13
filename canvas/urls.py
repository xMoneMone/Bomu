from django.urls import path, include
from canvas import views

urlpatterns = [
    path('create', views.canvas, name="canvas"),
    path('post', views.post_canvas, name="post-canvas"),
    path('palettes', views.palettes, name="palettes"),
    path('palettes/add', views.palette_add, name="add palette"),
    path('palette/edit/<int:pk>', views.palette_edit, name="edit palette"),
    path('palette/delete/<int:pk>', views.palette_delete, name="delete palette")
]
