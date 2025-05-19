from django.dispatch import receiver
from django.contrib.auth import get_user_model
from allauth.socialaccount.signals import social_account_added
from allauth.account.signals import user_signed_up  # For regular signups

User = get_user_model()


@receiver(social_account_added)
def populate_user_profile(request, sociallogin, **kwargs):
    """
    Handle social account additions (like Google login)
    """
    user = sociallogin.user

    # Set default values for your custom fields
    if not user.gender:
        user.gender = "other"
    if not user.gym_place:
        user.gym_place = "Unknown"

    # Handle Google-specific data
    if sociallogin.account.provider == "google":
        extra_data = sociallogin.account.extra_data
        if "given_name" in extra_data:
            user.first_name = extra_data.get("given_name", "")
        if "family_name" in extra_data:
            user.last_name = extra_data.get("family_name", "")

    user.save()


@receiver(user_signed_up)
def handle_regular_signup(request, user, **kwargs):
    """
    Handle regular (non-social) signups if needed
    """
    # Set default values for your custom fields
    if not user.gender:
        user.gender = "other"
    if not user.gym_place:
        user.gym_place = "Unknown"
    user.save()
