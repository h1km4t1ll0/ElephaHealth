from django import forms
from django.contrib.auth.forms import UserCreationForm
from .chill_app.models import User


class NewUserForm (UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "phone_number", "company", "date_of_birth", "gender", "height", "weight",
                  "avg_heart_rate")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
