from django.urls import path
from . import views

app_name = "user"  # This sets the namespace 'user'

urlpatterns = [path("register/", views.register, name="register")]
