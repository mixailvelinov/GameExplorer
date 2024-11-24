from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.managers import AccountManager
from accounts.validators import name_validator

# Create your models here.


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = AccountManager()


class Profile(models.Model):
    user = models.OneToOneField(
        'accounts.Account',
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(max_length=30, null=True, blank=True, validators=[name_validator])
    last_name = models.CharField(max_length=30, null=True, blank=True, validators=[name_validator])
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
