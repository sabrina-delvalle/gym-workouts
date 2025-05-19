from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
import requests

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)

        # Set default values for required fields
        user.gender = "other"  # default gender
        user.gym_place = "Unknown"  # default gym place

        # Get profile picture from Google if available
        if sociallogin.account.provider == "google":
            extra_data = sociallogin.account.extra_data
            if "picture" in extra_data:
                try:
                    response = requests.get(extra_data["picture"])
                    if response.status_code == 200:
                        user.pic.save(
                            f"{user.username}_google.jpg",
                            ContentFile(response.content),
                            save=False,
                        )
                except:  # noqa: E722
                    pass

        return user
