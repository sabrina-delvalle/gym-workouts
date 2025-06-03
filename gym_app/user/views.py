from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login  # UserCreationForm
from django.contrib import messages  # logout
from django.views.decorators.csrf import csrf_exempt
from .models import User
from . import forms
import json

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
        "user/profile.html",
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


@csrf_exempt  # Remove in production and use proper CSRF protection
@login_required
def save_workout(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print("Received workout data:", data)

            # Get the user object (assuming your User model has
            # a selection field) #flake8
            user = request.user

            # Update the selection field
            user.selection = data
            user.save()

            return JsonResponse({"status": "success"})

        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)}, status=400
            )  # flake8

    return JsonResponse(
        {"status": "error", "message": "Invalid request"}, status=400
    )  # flake8


@csrf_exempt  # Remove in production
@login_required
def delete_workout(request):
    if request.method == "POST":
        try:
            # Get the authenticated user
            user = request.user

            # Clear the selection field
            user.selection = {}  # Or set to None if your field allows it
            user.save()

            return JsonResponse(
                {"status": "success", "message": "Workout data cleared"}
            )

        except Exception as e:
            return JsonResponse(
                {"status": "error", "message": str(e)}, status=400
            )  # flake8

    return JsonResponse(
        {"status": "error", "message": "Invalid request"}, status=400
    )  # flake8
