from django import forms
from .models import User
from django.contrib.auth.hashers import make_password


class CreateUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "username", "email", "gender", "password", "gym_place"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])  # Hash password
        if commit:
            user.save()
        return user
