from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CustomUser(User):
    _username = models.CharField(max_length=150, unique=True)
    _first_name = models.CharField(max_length=100, blank=True)
    _last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=30, default='+996')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=100, choices=(('M', 'Male'),
                                                       ('F', 'Female'),
                                                       ('O', 'Other')))
    profession = models.CharField(max_length=200, blank=True)
    _email = models.EmailField(max_length=254, unique=True)
    _is_staff = models.BooleanField(default=False)
    _date_joined = models.DateTimeField(default=timezone.now)





