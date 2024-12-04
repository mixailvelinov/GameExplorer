from django.contrib import admin

from accounts.forms import AccountRegisterForm
from accounts.models import Account, Profile


# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fieldsets = (
         (None, {'fields': ('email', 'password')}),
         ('Permissions', {'fields': ('is_active', 'is_staff', 'groups',
        'user_permissions')}),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass