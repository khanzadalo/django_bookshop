from django import forms
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from . import models


class CustomUserCreationForm(UserCreationForm):
    _username = forms.CharField(max_length=150, required=True)
    _first_name = forms.CharField(max_length=150)
    _last_name = forms.CharField(max_length=150)
    _email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996',
                                   widget=forms.TextInput(attrs={'placeholder': 'enter the phone number'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=(('M', 'Male'),
                                        ('F', 'Female'),
                                        ('O', 'Other')))
    profession = forms.CharField(max_length=200)
    _is_staff = forms.BooleanField(required=False, initial=False)
    _date_joined = forms.DateField(initial=timezone.now)

    class Meta:
        model = models.CustomUser
        fields = ("_username",
                  "_first_name",
                  "_last_name",
                  "_email",
                  "phone_number",
                  "date_of_birth",
                  "gender",
                  "profession",
                  "_is_staff",
                  "_date_joined")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['_first_name']
        user.last_name = self.cleaned_data['_last_name']
        user.email = self.cleaned_data['_email']
        if commit:
            user.save()
            return user






