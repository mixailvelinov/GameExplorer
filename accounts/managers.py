from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Group


class AccountManager(auth_models.BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("You can't register without an email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

    # def create_moderator(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', False)
    #
    #     user = self.create_user(email, password, **extra_fields)
    #
    #     moderators_group, created = Group.objects.get_or_create(name="Moderators")
    #     user.groups.add(moderators_group)
    #
    #     return user

