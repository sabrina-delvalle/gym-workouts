from django.db import models

# from django.contrib.auth.models import User


class User(models.Model):
    first_name = models.CharField(max_length=55)
    username = models.CharField(max_length=55)
    email = models.EmailField(max_length=255)
    GENDERS_ = (("option1", "male"), ("option2", "female"), ("option3", "other"))
    gender = models.CharField(max_length=10, choices=GENDERS_)
    password = models.CharField(max_length=155)
    gym_place = models.CharField(max_length=255)
    pic = models.ImageField(default="user-profile.png", blank=True)
    selection = models.JSONField(default=dict)

    def __str__(self):
        return self.first_name
