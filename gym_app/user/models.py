from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Remove these fields since they're already in AbstractUser:
    # first_name (inherited)
    # username (inherited)
    # email (inherited)
    # password (inherited - properly hashed)

    GENDERS = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )
    gender = models.CharField(max_length=10, choices=GENDERS)
    gym_place = models.CharField(max_length=255)
    pic = models.ImageField(default="user-profile.png", blank=True)
    selection = models.JSONField(default=dict)

    # Add any custom methods you need
    def __str__(self):
        return self.get_full_name() or self.username
