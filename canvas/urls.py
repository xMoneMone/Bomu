from django.urls import path, include
from canvas import views

urlpatterns = [
    path('create', views.canvas, name="canvas"),
]
