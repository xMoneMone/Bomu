from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('new', views.home_new, name="home-new")
]

