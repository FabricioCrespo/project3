
#=============================PROJECT 3========================================
#==========================WEB PROGRAMMING========================
#=========================NAME: JONNATHAN FABRICIO CRESPO YAGUANA=============
#==========================DATE: DECEMBER 2019=================================

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("login", auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
