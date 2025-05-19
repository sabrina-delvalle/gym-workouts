from django.urls import path
from .views import profile
from . import views

app_name = "user"  # This sets the namespace 'user'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("profile/", profile, name="profile"),
]
