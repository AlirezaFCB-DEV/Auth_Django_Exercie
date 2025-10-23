from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view , profile_view

app_name = "accounts"

url_patterns = [
    path("login/" , auth_views.LoginView.as_view(template_name = "account/login.html") , name = "login"),
    path("logout/" , auth_views.LogoutView.as_view(next_page ="accounts.login") , name="logout"),
    path("register/" , register_view , name="register"),
    path("profile/" , profile_view , name="profile")
]