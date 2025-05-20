# from django.http import HttpResponse
from django.shortcuts import render


# def homepage(request):
# return HttpResponse("Home Index")
# return render(request, "index.html")


def homepage(request):
    # Check if this is a social account
    social_account = (
        request.user.socialaccount_set.first()
        if hasattr(request.user, "socialaccount_set")
        else None
    )

    return render(
        request,
        "index.html",
        {"user": request.user, "social_account": social_account},
    )
