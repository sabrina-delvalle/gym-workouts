from django.shortcuts import render, redirect
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
