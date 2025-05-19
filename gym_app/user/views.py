from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import authenticate, login  # UserCreationForm
from django.contrib import messages  # logout
from . import forms

# from django.contrib.auth import login


# Create your views here.
def register(request):
    if request.method == "POST":
        print("Form submitted!")
        form = forms.CreateUser(request.POST)
        if form.is_valid():
            print("Form is valid!")  # Check if validation passes
            form.save()
            print("User created: ")  # Verify creation
            return redirect("index")
        else:
            print("Form errors:", form.errors)  # Log validation errors
    else:
        form = forms.CreateUser()
    return render(request, "user/register.html", {"form": form})


@login_required
def profile(request):
    # Check if this is a social account
    social_account = (
        request.user.socialaccount_set.first()
        if hasattr(request.user, "socialaccount_set")
        else None
    )

    return render(
        request,
        "accounts/profile.html",
        {"user": request.user, "social_account": social_account},
    )


def login_view(request):
    username = request.POST.get("username")  # Ensure lowercase
    password = request.POST.get("password")
    try:
        user = User.objects.get(username=username)
        print(f"User found: {user}, Active: {user.is_active}")
        print(f"Password matches: {user.check_password(password)}")
    except User.DoesNotExist:
        print("User does not exist!")

    if request.method == "POST":
        username = request.POST.get("username")  # Ensure lowercase
        password = request.POST.get("password")

        # Authenticate the user (checks password)
        user = authenticate(request, username=username, password=password)
        print("user... ", user)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "user/login.html")
