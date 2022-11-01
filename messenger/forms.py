from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile
from django import forms


class NewUserForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        print("NewUserForm:save")
        user = super(NewUserForm, self).save(commit=False)
        # user.email = self.cleaned_data['email']

        if commit:
            print("committing user")
            user.save()

        return user
