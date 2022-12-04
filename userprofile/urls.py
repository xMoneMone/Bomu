from django.urls import path, include
from userprofile import views

urlpatterns = [
    path('signup', views.usersignup, name="signup"),
    path('login', views.userlogin, name="login"),
    path('logout', views.userlogout, name="logout"),
    path('edit-profile', views.useredit, name="edit profile"),
    path('delete', views.userdelete, name="delete profile"),
    path('<uname>', views.ShowProfile.as_view(), name="show profile"),
]
